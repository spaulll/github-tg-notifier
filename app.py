import os
import json
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
GITHUB_SECRET = "YOUR_GITHUB_WEBHOOK_SECRET"

@app.route("/github-webhook", methods=["POST"])
def githubWebhook():
    if request.method == "POST":
        payload = request.json
        event = request.headers.get("X-GitHub-Event")
        
        message = f"GitHub Event: {event}"
        
        if event == "push":
            repo_name = payload["repository"]["full_name"]
            sender = payload["sender"]["login"]
            message += f"\n{sender} pushed to {repo_name}"
        
        send_telegram_message(message)
        return "Received GitHub event", 200

def sendToTG(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print("Failed to send Telegram message")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
