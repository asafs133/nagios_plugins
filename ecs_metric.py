import boto3
import datetime
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--namespace', action='store', dest='namespace',
                    help='CloudWatch namespaces are containers for metrics. For example: AWS/ECS')
parser.add_argument('--metricname', action='store', dest='metricname',
                    help='Metrics are data about the performance of your systems. For example: MemoryUtilization')
parser.add_argument('--clustername', action='store', dest='clustername',
                    help='This dimension filters the data you request for all resources in a specified cluster.')
parser.add_argument('--servicename', action='store', dest='servicename',
                    help='This dimension filters the data you request for all resources in a specified service within a specified cluster.')
parser.add_argument('--period', action='store', dest='period', type=int,
                    help='A period is the length of time associated with a specific Amazon CloudWatch statistic. For example, to specify a period of 5 minutes, use 300 as the period value.')
parser.add_argument('--statistics', action='store', dest='statistics',
                    help='Statistics are metric data aggregations over specified periods of time. For example: Average')
parser.add_argument('--unit', action='store', dest='unit',
                    help='Each statistic has a unit of measure. For example: Percent')
parser.add_argument('--ok_threshold', action='store', dest='ok_threshold', type=float,
                    help='Threshold which reflects the OK status value.')
parser.add_argument('--warning_threshold', action='store', dest='warning_threshold', type=float,
                    help='Threshold which reflects the Warning status value.')
parser.add_argument('--critical_threshold', action='store', dest='critical_threshold', type=float,
                    help='Threshold which reflects the Critical status value.')

args_res = parser.parse_args()


#get arguments from the client
AWS_Namespace = args_res.namespace
AWS_MetricName = args_res.metricname
AWS_ClusterName = args_res.clustername
AWS_ServiceName = args_res.servicename
AWS_Period = args_res.period
AWS_Statistics = args_res.statistics
AWS_Unit = args_res.unit
OK_Status = args_res.ok_threshold
Warning_Status = args_res.warning_threshold
Critical_Status = args_res.critical_threshold

client = boto3.client('cloudwatch')

response = client.get_metric_statistics(
    Namespace=AWS_Namespace,
    MetricName=AWS_MetricName,
    Dimensions=[
            {
                'Name':'ClusterName',
                'Value':AWS_ClusterName
            },
            {
                'Name':'ServiceName',
                'Value':AWS_ServiceName
             },
        ],
    StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=5),#Number of metric data to recieve for example 5 = 1 metric
    EndTime=datetime.datetime.utcnow(),
    Period=AWS_Period,#get metric data by time, for example 3600 = 1 hour
    Statistics=[AWS_Statistics],
    Unit=AWS_Unit
)

for val in response['Datapoints']:
    Var_Result = float(val['Average'])

if Var_Result < OK_Status:
        print("OK - %s = %s." % (AWS_MetricName, Var_Result))
        sys.exit(0)
elif Var_Result >= Warning_Status and Var_Result < Warning_Status+10:
        print("WARNING - %s = %s." % (AWS_MetricName, Var_Result))
        sys.exit(1)
elif Var_Result >= Critical_Status:
        print("CRITICAL - %s = %s." % (AWS_MetricName, Var_Result))
        sys.exit(2)
else:
        print("UKNOWN - %s = %s." % (AWS_MetricName, Var_Result))
        sys.exit(3)
