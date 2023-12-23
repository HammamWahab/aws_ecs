import boto3

# Replace this with your cluster name
cluster_name = 'your-cluster-name-1'

ecs = boto3.client('ecs')

# Delete the ECS cluster
response = ecs.delete_cluster(
    cluster=cluster_name
)

print(f"Cluster '{cluster_name}' deletion status: {response['cluster']['status']}")
