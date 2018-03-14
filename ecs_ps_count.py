#!/usr/bin/env python3
import boto3
import sys
import argparse

# Author: Asaf Shabat

parser = argparse.ArgumentParser()
parser.add_argument('--clustername', action='store', dest='clustername',
                    help='This dimension filters the data you request for all resources in a specified cluster.')
parser.add_argument('--ok_threshold', action='store', dest='ok_threshold', type=float,
                    help='Threshold which reflects the OK status value.')
parser.add_argument('--critical_threshold', action='store', dest='critical_threshold', type=float,
                    help='Threshold which reflects the Critical status value.')

args_res = parser.parse_args()

# get arguments from the client
AWS_ClusterName = args_res.clustername
OK_Status = args_res.ok_threshold
Critical_Status = args_res.critical_threshold

client = boto3.client('ecs')
tasks = client.list_tasks(cluster=AWS_ClusterName)
ContainerCounter = len(tasks['taskArns'])

if ContainerCounter >= OK_Status:
    print("OK - %s contains %s containers alive!" % (AWS_ClusterName, ContainerCounter))
    sys.exit(0)
elif ContainerCounter < Critical_Status:
    print("CRITICAL - %s contains %s containers alive!" % (AWS_ClusterName, ContainerCounter))
    sys.exit(2)
else:
    print("UNKNOWN - %s contains %s containers alive!" % (AWS_ClusterName, ContainerCounter))
    sys.exit(3)
