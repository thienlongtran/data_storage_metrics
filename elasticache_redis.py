import random
import boto3
from redis import Redis

elasticache_client = boto3.client("elasticache")
elasticache_cluster_name = "project-talia"

def create_cluster():
    response = elasticache_client.create_cache_cluster(
            CacheClusterId = elasticache_cluster_name,
            Engine = "redis",
            CacheNodeType = "cache.t2.micro",
            NumCacheNodes = 1
        )

    return response

def generate_and_add_data():
    redis = Redis(host="project-talia.kggewh.0001.use1.cache.amazonaws.com", port=6379, decode_responses=True, ssl=True, username='myuser', password='MyPassword0123456789')
    redis.set('foo', 'bar')

    JOB_IDS = range(100000)
    JOB_STATUSES = ["queued", "in_progress", "completed", "completed", "completed", "completed"]

    for id in JOB_IDS:
        workflow_job = {
            "job_id": {"N": str(id)},
            "status": {"S": random.choice(JOB_STATUSES)},
            "repository": {"S": "testing123"},
            "started_at": {"S": "blankblankblank"},
            "starteat": {"S": "blankblankblank"},
            "star323": {"S": "blankblankblank"},
            "fwafewagf": {"S": "blankblankblank"}
        }

        response = dynamodb_client.put_item(
            TableName = dynamodb_table_name,
            Item = workflow_job
        )

if __name__ == "__main__":
    #create_cluster()
    generate_and_add_data()
