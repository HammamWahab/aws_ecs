## Deploy image using ECS 

Assuming you have a cluster on ecs, you can create a service using:
`python3 src/create_ecs_services.py`

### ToDo: 
- Create 2 security groups 
    a. One with inbound only 80.
    b. One with only security group (a).
- Create an application load balancer and attatch it to the created server. 
