import boto3

# Replace these values with your own
cluster_name = 'your-cluster-name'
task_definition_name = 'your-task-definition-name'
service_name = 'your-service-name'
desired_task_count = 1  # Number of tasks to run
alb_name = 'your-alb-name'
target_group_name = 'your-target-group-name'
container_name = 'your-container-name'
container_image = 'your-container-image'

ecs = boto3.client('ecs')
elbv2 = boto3.client('elbv2')

# Register the task definition
response = ecs.register_task_definition(
    family=task_definition_name,
    containerDefinitions=[
        {
            'name': container_name,
            'image': container_image,
            'memory': 128,
            'memoryReservation': 64,
            # Add other container configuration as needed
        },
    ],
)

# Get the task definition ARN
task_definition_arn = response['taskDefinition']['taskDefinitionArn']

# Create or update the service
response = ecs.create_service(
    cluster=cluster_name,
    serviceName=service_name,
    taskDefinition=task_definition_arn,
    desiredCount=desired_task_count,
    launchType='EC2',  # Change to 'FARGATE' if you're using Fargate
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': ['subnet-id-1', 'subnet-id-2'],  # Replace with your subnet IDs
            'securityGroups': ['security-group-id'],  # Replace with your security group ID
        }
    },
    healthCheckGracePeriodSeconds=60,
    enableExecuteCommand=True,
    loadBalancers=[
        {
            'targetGroupArn': 'arn:aws:elasticloadbalancing:region:account-id:targetgroup/' + target_group_name,
            'containerName': container_name,
            'containerPort': 80,  # Change to the port your container is listening on
        },
    ],
)

print(f"Service '{service_name}' deployment status: {response['service']['status']}")
