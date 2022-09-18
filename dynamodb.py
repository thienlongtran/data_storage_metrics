import random
import boto3
from boto3.dynamodb.conditions import Key

dynamodb_client = boto3.client("dynamodb")
dynamodb_table_name = "project-talia"

def create_table():
    response = dynamodb_client.create_table(
            AttributeDefinitions = [
                {
                    "AttributeName": "job_status",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "job_id",
                    "AttributeType": "N"
                }
            ],
            TableName = dynamodb_table_name,
            KeySchema = [
                {
                    "AttributeName": "job_status",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "job_id",
                    "KeyType": "RANGE"
                }
            ],
            BillingMode = "PAY_PER_REQUEST"
        )

    return response

def generate_and_add_data():
    JOB_IDS = range(30000)
    JOB_STATUSES = ["queued", "in_progress", "completed", "completed", "completed", "completed", "completed", "completed", "completed", "completed"]

    for id in JOB_IDS:
        workflow_job = {
            "job_id": {"N": str(id)},
            "job_status": {"S": random.choice(JOB_STATUSES)},
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

def get_items(status):
    response = dynamodb_client.query(
        TableName = dynamodb_table_name,
        KeyConditionExpression = "job_status = :target_status",
        ExpressionAttributeValues={":target_status": {"S": status}}
    )

    seen = {}

    for item in response["Items"]:
        seen[item["job_id"]["N"]] = {
            "status": item["job_status"]["S"],
            "repository": item["repository"]["S"],
            "started_at": item["started_at"]["S"],
            "starteat": item["starteat"]["S"],
            "star323": item["star323"]["S"],
            "fwafewagf": item["fwafewagf"]["S"]
        }
        
    print(len(seen))

if __name__ == "__main__":
    #create_table()
    #generate_and_add_data()
    get_items("queued")
