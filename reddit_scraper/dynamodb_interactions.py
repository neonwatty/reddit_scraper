from reddit_scraper import main_dir
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# define boto3 session based on whether code executed in lambda
if "AWS_LAMBDA_FUNCTION_NAME" in os.environ:
    session = boto3.session.Session()
else:
    session = boto3.session.Session(profile_name=os.getenv("AWS_PROFILE"))
dynamodb_resource = session.resource("dynamodb", region_name="us-west-2")


def put_rows(rows: list, table_name: str = "metrics-reddit") -> None:
    try:
        table = dynamodb_resource.Table(table_name)
        for row in rows:
            response = table.put_item(Item=row)
            assert (
                response["ResponseMetadata"]["HTTPStatusCode"] == 200
            ), f"FAILURE: row failed to put {row}"
        print("SUCCESS: put_rows successfully")
    except Exception as e:
        print(f"FAILURE: put_rows failed to put with exception {e}")
        return None


def create_table(table_name: str):
    try:
        # Define the key schea
        key_schema = [
            {"AttributeName": "reddit_url", "KeyType": "HASH"},
            {"AttributeName": "timestamp", "KeyType": "RANGE"},
        ]

        # Define the attribute definitions
        attribute_definitions = [
            {"AttributeName": "reddit_url", "AttributeType": "S"},
            {"AttributeName": "timestamp", "AttributeType": "N"},
        ]

        # Create the table
        table = dynamodb_resource.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            BillingMode="PAY_PER_REQUEST",
        )

        # Wait for the table to be created (optional)
        table.wait_until_exists()
        return True
    except Exception as e:
        print("FAILURE: Error creating table: ", e)
        return False
