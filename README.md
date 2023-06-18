
# Twitter Data Pipeline

In this project I created a fully automated pipeline that loads tweets data from twitter using twitter APIs, transforms the data into desired format and loads this data into AWS S3 buckets.

This process runs over a certain interval of time. This  is scheduled via airflow jobs which are deployed over AWS EC2 instances.


