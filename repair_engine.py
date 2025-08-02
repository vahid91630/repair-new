# repair_engine.py
import requests
import os
import json

BOT_MONITOR_FILE = "bot_status.json"

def load_bots_to_repair():
    if not os.path.exists(BOT_MONITOR_FILE):
        print("❌ فایل bot_status.json یافت نشد.")
        return []

    with open(BOT_MONITOR_FILE, "r") as f:
        data = json.load(f)
    return [bot for bot in data.get("bots", []) if bot["status"] == "Needs Repair"]

def start_repair():
    bots = load_bots_to_repair()
    if not bots:
        print("✅ هیچ باتی نیاز به تعمیر ندارد.")
        return

    for bot in bots:
        response = requests.post(
            os.getenv("REPAIR_API_URL"),
            headers={"Authorization": f"Bearer {os.getenv('REPAIR_API_KEY')}"},
            json={"bot_id": bot["id"]}
        )
        print(f"📤 ارسال تعمیر برای {bot['id']}: {response.status_code} - {response.text}")
