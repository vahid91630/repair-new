# deploy_notifier.py
import requests
import os

def send_deploy_notification(bot_id):
    response = requests.post(
        os.getenv("DEPLOY_API_URL"),
        headers={"Authorization": f"Bearer {os.getenv('DEPLOY_API_KEY')}"},
        json={"bot_id": bot_id, "status": "Healthy"}
    )
    print(f"🚀 Deploy info sent: {response.status_code} - {response.text}")
