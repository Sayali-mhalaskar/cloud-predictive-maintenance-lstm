
from app import app

def lambda_handler(event, context):
    path = event.get("rawPath", "/")
    if path == "/":
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "https://main.dyii2vtupy0th.amplifyapp.com"
            },
            "body": '{"message":"Flask API package required"}'
        }

    return {
        "statusCode": 503,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://main.dyii2vtupy0th.amplifyapp.com"
        },
        "body": '{"error":"Backend deployment is incomplete"}'
    }
