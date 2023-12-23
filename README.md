# Deploy images on AWS using ECS 

### To do on AWS UI: 
- Create 2 security groups 
    a. One with inbound only 80.
    b. One with only security group (a).
- Create the Application Load Balancer

### Create the ECS Service
Assuming you have a cluster on ecs and an application load balancer, you can create a service using:
`python3 src/create_ecs_services.py`


