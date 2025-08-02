# repair_worker.py
import requests
import os

def fetch_repair_status(bot_id):
    response = requests.get(
        f"{os.getenv('REPAIR_API_URL')}/{bot_id}/status",
        headers={"Authorization": f"Bearer {os.getenv('REPAIR_API_KEY')}"}
    )
    return response.json()

def finalize_repair(bot_id):
    status = fetch_repair_status(bot_id)
    if status.get("repaired", False):
        print(f"✅ بات {bot_id} تعمیر شد.")
        notify_deployment(bot_id)
    else:
        print(f"⚠️ تعمیر بات {bot_id} هنوز کامل نشده.")

def notify_deployment(bot_id):
    response = requests.post(
        os.getenv("DEPLOY_API_URL"),
        headers={"Authorization": f"Bearer {os.getenv('DEPLOY_API_KEY')}"},
        json={"bot_id": bot_id, "status": "Healthy"}
    )
    print(f"📢 اطلاع‌رسانی deploy برای {bot_id}: {response.status_code}")
