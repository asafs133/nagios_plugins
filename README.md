## ecs_metric.py
### Objective 
- Get metrics of [AWS ECS](https://aws.amazon.com/ecs/) Memory & CPU.
- This plugin exist & approved by [Nagios Exchange](https://exchange.nagios.org/directory/Plugins/Cloud/ECS-cluster-and-service-monitor/details).

### Prerequisites 
- Python3
- boto3 extention (using: pip install boto3)
- AWS cli [installed](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- AWS Access key, Secret key and Region [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

### Usage 
```
./ecs_metric.py [-h] [--namespace NAMESPACE] [--metricname METRICNAME] [--clustername CLUSTERNAME]
                     [--servicename SERVICENAME] [--period PERIOD] [--statistics STATISTICS]
                     [--unit UNIT] [--ok_threshold OK_THRESHOLD] [--warning_threshold WARNING_THRESHOLD]
                     [--critical_threshold CRITICAL_THRESHOLD]
```

### Arguments  

`-h, --help`  
  Show this help message and exit  
  
`--namespace NAMESPACE`  
CloudWatch namespaces are containers for metrics.  
For example: AWS/ECS  

`--metricname METRICNAME`  
Metrics are data about the performance of your systems.  
For example: MemoryUtilization  

`--clustername CLUSTERNAME`  
This dimension filters the data you request for all resources in a specified cluster.

`--servicename SERVICENAME`  
This dimension filters the data you request for all resources in a specified service within a specified cluster.
          
`--period PERIOD `  
A period is the length of time associated with a specific Amazon CloudWatch statistic.  
For example: to specify a period of 5 minutes, use 300 as the period value.  
                        
`--statistics STATISTICS`  
Statistics are metric data aggregations over specified periods of time.  
For example: Average  
                        
`--unit UNIT`  
Each statistic has a unit of measure.  
For example: Percent  

`--ok_threshold OK_THRESHOLD`  
Threshold which reflects the OK status value.  

`--warning_threshold WARNING_THRESHOLD`  
Threshold which reflects the Warning status value.  

`--critical_threshold CRITICAL_THRESHOLD`  
Threshold which reflects the Critical status value.
