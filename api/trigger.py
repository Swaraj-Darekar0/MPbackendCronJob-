import requests
import os

def handler(request):
    url = "https://moneypath-bacekend.onrender.com/api/cron/trigger-discipline-engine"
    headers = {
        "Content-Type": "application/json",
        "x-cron-secret": os.environ.get("CRON_SECRET")
    }

    try:
        response = requests.post(url, headers=headers)
        return {
            "statusCode": 200,
            "body": f"Triggered. Status: {response.status_code}, Response: {response.text}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
