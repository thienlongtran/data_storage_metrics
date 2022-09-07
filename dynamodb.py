import random
import boto3

dynamodb_client = boto3.client("dynamodb")
dynamodb_table_name = "project-talia"

def create_table():
    response = dynamodb_client.create_table(
            AttributeDefinitions = [
                {
                    "AttributeName": "job_id",
                    "AttributeType": "N"
                },
                {
                    "AttributeName": "status",
                    "AttributeType": "S"
                }
            ],
            TableName = dynamodb_table_name,
            KeySchema = [
                {
                    "AttributeName": "job_id",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "status",
                    "KeyType": "RANGE"
                }
            ],
            BillingMode = "PAY_PER_REQUEST"
        )

    return response

def generate_and_add_data():
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
    create_table()
    generate_and_add_data()
