from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ganti dengan App ID & Secret kamu
APP_ID = "cli_a7394424f1bb102f"
APP_SECRET = "2drZpQ7UxJEnmzedcrOgfgsPCBjjUozv"

@app.route("/", methods=["GET"])
def home():
    return "Lark Auto-Reply Bot is Running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    # Cek jika event adalah pesan masuk
    if "event" in data and data["event"]["type"] == "message":
        chat_id = data["event"]["message"]["chat_id"]
        send_message(chat_id)

    return jsonify({"status": "ok"})

def send_message(chat_id):
    url = "https://open.larksuite.com/open-apis/im/v1/messages"
    headers = {
        "Authorization": f"Bearer {APP_ID}:{APP_SECRET}",
        "Content-Type": "application/json"
    }
    data = {
        "receive_id": chat_id,
        "msg_type": "text",
        "content": '{"text": "Maaf, lama merespon. Untuk sementara bisa bertanya kepada SmartHR untuk pertanyaan Anda."}'
    }
    requests.post(url, json=data, headers=headers)

if __name__ == "__main__":
    app.run(port=5000)
