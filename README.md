# nagios_plugins
Nagios plugins - Python script repository

========================ecs_metric.py==========================

- Get metrics of ECS Memory & CPU.
- The script uses boto3 extention, so you have to verify that ~/.aws/credentials has exist & initialized by aws_secret_access_key, aws_access_key_id.
- The script uses Python3 version.
- You have to install awscli (using pip) and initialize it by aws configure in order to create the credentails file and set the AWS region.

usage: ecs_metric.py [-h] [--namespace NAMESPACE] [--metricname METRICNAME]
                     [--clustername CLUSTERNAME] [--servicename SERVICENAME]
                     [--period PERIOD] [--statistics STATISTICS] [--unit UNIT]
                     [--ok_threshold OK_THRESHOLD]
                     [--warning_threshold WARNING_THRESHOLD]
                     [--critical_threshold CRITICAL_THRESHOLD]

optional arguments:

  -h, --help            show this help message and exit
  
  --namespace NAMESPACE
                        CloudWatch namespaces are containers for metrics. For
                        example: AWS/ECS
                        
  --metricname METRICNAME
                        Metrics are data about the performance of your
                        systems. For example: MemoryUtilization
                        
  --clustername CLUSTERNAME
                        This dimension filters the data you request for all
                        resources in a specified cluster.
                        
  --servicename SERVICENAME
                        This dimension filters the data you request for all
                        resources in a specified service within a specified
                        cluster.
                        
  --period PERIOD       A period is the length of time associated with a
                        specific Amazon CloudWatch statistic. For example, to
                        specify a period of 5 minutes, use 300 as the period
                        value.
                        
  --statistics STATISTICS
                        Statistics are metric data aggregations over specified
                        periods of time. For example: Average
                        
  --unit UNIT           Each statistic has a unit of measure. For example:
                        Percent
                        
  --ok_threshold OK_THRESHOLD
                        Threshold which reflects the OK status value.
                        
  --warning_threshold WARNING_THRESHOLD
                        Threshold which reflects the Warning status value.
                        
  --critical_threshold CRITICAL_THRESHOLD
                        Threshold which reflects the Critical status value.