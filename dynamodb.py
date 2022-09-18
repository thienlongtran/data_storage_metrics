import random
import boto3

dynamodb_client = boto3.client("dynamodb")
dynamodb_table_name = "project-talia"

def create_table():
    response = dynamodb_client.create_table(
            AttributeDefinitions = [
                {
                    "AttributeName": "status",
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
                    "AttributeName": "status",
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

def get_items(status):
    response = dynamodb_client.scan(
        TableName = dynamodb_table_name,
        ScanFilter = {"status": {
            "ComparisonOperator": "EQ",
            "AttributeValueList": [ {"S": "queued"} ]
        }}
    )

    seen = {}

    for item in response["Items"]:
        seen[item["job_id"]["N"]] = {
            "status": item["status"]["S"],
            "repository": item["repository"]["S"],
            "started_at": item["started_at"]["S"],
            "starteat": item["starteat"]["S"],
            "star323": item["star323"]["S"],
            "fwafewagf": item["fwafewagf"]["S"]
        }
        
    print(seen)

if __name__ == "__main__":
    #create_table()
    generate_and_add_data()
    #get_items("queued")
