#!/usr/bin/env python3
#Author: Asaf Shabat
import boto3
import datetime
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--targetgroup', action='store', dest='targetgroup',
                    help='Each target group is used to route requests to one or more registered targets. For example: targetgroup/target-group-name/numbers&characters')
parser.add_argument('--loadbalancer', action='store', dest='loadbalancer',
                    help='The load balancer distributes incoming application traffic across multiple targets. For example: app/application-load-balancer/numbers&characters')
parser.add_argument('--period', action='store', dest='period', type=int,
                    help='A period is the length of time associated with a specific Amazon CloudWatch statistic. For example, to specify a period of 5 minutes, use 300 as the period value.')
parser.add_argument('--statistics', action='store', dest='statistics',
                    help='Statistics are metric data aggregations over specified periods of time. For example: Average')
parser.add_argument('--unit', action='store', dest='unit',
                    help='Each statistic has a unit of measure. For example: Count')
parser.add_argument('--ok_threshold', action='store', dest='ok_threshold', type=float,
                    help='Threshold which reflects the OK status value.')
parser.add_argument('--critical_threshold', action='store', dest='critical_threshold', type=float,
                    help='Threshold which reflects the Critical status value.')


args_res = parser.parse_args()


#get arguments from the client
AWS_TargetGroup = args_res.targetgroup
AWS_LoadBalancer = args_res.loadbalancer
AWS_Period = args_res.period
AWS_Statistics = args_res.statistics
AWS_Unit = args_res.unit
OK_Status = args_res.ok_threshold
Critical_Status = args_res.critical_threshold

client = boto3.client('cloudwatch')

response = client.get_metric_statistics(
    Namespace='AWS/ApplicationELB',
    MetricName='UnHealthyHostCount',
    Dimensions=[
            {
                'Name':'TargetGroup',
                'Value':AWS_TargetGroup
            },
            {
                'Name':'LoadBalancer',
                'Value':AWS_LoadBalancer
            },
        ],
    StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=5),
    EndTime=datetime.datetime.utcnow(),
    Period=AWS_Period,
    Statistics=[AWS_Statistics],
    Unit=AWS_Unit
)

for val in response['Datapoints']:
    Var_Result = float(val[AWS_Statistics])

if Var_Result == OK_Status:
        print("OK - %s = %s" % ('UnHealthyHostCount', Var_Result))
        sys.exit(0)
elif Var_Result > Critical_Status:
        print("CRITICAL - %s = %s" % ('UnHealthyHostCount', Var_Result))
        sys.exit(2)
else:
        print("UNKNOWN - %s = %s" % ('UnHealthyHostCount', Var_Result))
        sys.exit(3)
