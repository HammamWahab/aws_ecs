import boto3

# Replace these values with your own
cluster_name = 'your-cluster-name-1'
task_definition_name = 'your-task-definition-name'
container_name = 'your-container-name'
service_name = 'your-service-name'
image_name = 'public.ecr.aws/nginx/nginx:stable-perl'

ecs = boto3.client('ecs')

# Create a new task definition
response = ecs.register_task_definition(
    family=task_definition_name,
    containerDefinitions=[
        {
            'name': container_name,
            'image': image_name,  # Leave this empty for now; we'll update it in the loop
            # Add other container configuration as needed
            'memory': 128,  # Specify the memory for the container
            'memoryReservation': 64,  # Specify the memory reservation for the container
        },
    ],
)

# Get the task definition ARN
task_definition_arn = response['taskDefinition']['taskDefinitionArn']

desired_task_count = 1  # Number of tasks to run

# Create or update the service
response = ecs.create_service(
    cluster=cluster_name,
    serviceName=service_name,
    taskDefinition=task_definition_arn,
    desiredCount=desired_task_count,
    # Add other service configuration as needed
)

print(f"Service '{service_name}' deployment status: {response['service']['status']}")


