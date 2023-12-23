# Deploy Images on AWS using ECS 

### To do on AWS UI: 
- Create 2 security groups 
    a. One with inbound only 80.
    b. One with only security group (a).
- Create the Application Load Balancer

### Prerequisites
- AWS Credentials `aws configure`
- Dependencies `pip install -r requirements.txt`
### Create the ECS Service
Assuming you have a cluster on ecs and an application load balancer, you can do the followings: 
- Adjust all infrastructure variables `src/create_ecs_services.py` & `src/delete_ecs_cluster.py`
- Create a service using: `python3 src/create_ecs_services.py`

### Delete the ECS Cluster 
`python3 src/delete_ecs_cluster.py`