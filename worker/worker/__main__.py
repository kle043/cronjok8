import argparse
import os
import requests
import time

JOB_SERVER_BASE_URL = os.environ['JOB_SERVER']

def main(args=None):

    parser = argparse.ArgumentParser()
    parser.add_argument('job_id', type=int, help='A job id')

    args = parser.parse_args(args)

    res = requests.post(f'{JOB_SERVER_BASE_URL}/worktime', json = {'id': int(args.job_id)})
    worker = res.json()
    print(f'Worker {worker["name"]} starts working!')
    time.sleep(worker['worktime'])
    print('Finished!')

if __name__ == "__main__":
  main()
