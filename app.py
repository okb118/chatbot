from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

import requests
import json

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    api_url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = "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"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://127.0.0.1:5000/",
        "X-Title": "ChatbotApp"
    }

    data = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [{"role": "user", "content": user_message}],
        "max_tokens": 100
    }

    print(f"API URL: {api_url}")
    print(f"Headers: {headers}")
    print(f"Payload: {data}")

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        reply = ("エラーが発生しました: {0}. "
                 "APIキーが無効な可能性があります。OpenRouterのダッシュボードでAPIキーを確認または再生成してください。").format(str(e))

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)