import os
import requests
from kubernetes import client, config
import time
import yaml

JOB_SERVER_BASE_URL = os.environ["JOB_SERVER"]
NAMESPACE = "default"

with open(os.path.join(os.path.dirname(__file__), "job-manifest.yaml")) as f:
    JOB_TEMPLATE = yaml.safe_load(f)


def to_k8_name(name):
    return name.lower().replace(" ", "space").replace("_", "-")


def create_job(batch_client, name, job_id, annotation):
    print(f"Start Creating job {name}")
    JOB_TEMPLATE["metadata"]["name"] = name
    JOB_TEMPLATE["metadata"]["annotations"] = annotation
    JOB_TEMPLATE["spec"]["template"]["spec"]["containers"][0]["command"] = [
        "worker",
        str(job_id),
    ]
    api_response = batch_client.create_namespaced_job(
        body=JOB_TEMPLATE, namespace=NAMESPACE
    )
    print("Job created. status='%s'" % str(api_response.status))


def delete_job(batch_client, name):
    api_response = batch_client.delete_namespaced_job(
        name=name,
        namespace=NAMESPACE,
        body=client.V1DeleteOptions(
            propagation_policy="Foreground", grace_period_seconds=5
        ),
    )
    print("Job deleted. status='%s'" % str(api_response.status))


def main(args=None):
    print('Starting')
    try:
        config.load_incluster_config()
        print('Using incluster config')
    except:
        # load_kube_config throws if there is no config, but does not document what it throws, so I can't rely on any particular type here
        print('Using kube config')
        config.load_kube_config()

    batch_client = client.BatchV1Api()
    current_jobs = batch_client.list_namespaced_job(
        NAMESPACE, label_selector="jobgroup=worker-group"
    )

    # Clean finished jobs, so that they can be restarted
    finished_job_names = [
        j.metadata.name for j in current_jobs.items if j.status.active is None
    ]

    for job_name in finished_job_names:
        print(f"Deleting {job_name}")
        delete_job(batch_client, job_name)

    time.sleep(5)

    running_job_names = [
        j.metadata.name for j in current_jobs.items if j.status.active is not None
    ]

    new_jobs = requests.get(f"{JOB_SERVER_BASE_URL}/characters").json()

    for job_id, name in zip(new_jobs["ids"], new_jobs["names"]):
        k8_name = to_k8_name(name)
        if k8_name not in running_job_names:
            create_job(batch_client, k8_name, job_id, {"name": name})
        else:
            print(f"{name} already working")

    print("Finished!")


if __name__ == "__main__":
    main()
