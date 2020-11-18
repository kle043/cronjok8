import argparse
import os
import requests
import time

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

JOB_SERVER_BASE_URL = os.environ['JOB_SERVER']
PROMETHEUS_SERVER = os.environ['PROMETHEUS_SERVER']

def main(args=None):

    print('Requesting data')
    parser = argparse.ArgumentParser()
    parser.add_argument('job_id', type=int, help='A job id')

    args = parser.parse_args(args)

    res = requests.post(f'{JOB_SERVER_BASE_URL}/worktime', json = {'id': int(args.job_id)})
    worker = res.json()
    print(f'Worker {worker["name"]} starts working!')
    for _ in range(0, worker['worktime']):
        print(f'{worker["name"]} working!')

    registry = CollectorRegistry()
    g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
    g.set_to_current_time()
    push_to_gateway(PROMETHEUS_SERVER, job=worker["name"], registry=registry)
    print('Finished!')

if __name__ == "__main__":
  main()
