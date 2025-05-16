from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # シンプルなルールベース応答
    if "こんにちは" in user_message:
        reply = "こんにちは！ご用件は何でしょうか？"
    elif "ありがとう" in user_message:
        reply = "どういたしまして！"
    elif "さようなら" in user_message:
        reply = "またお会いしましょう！"
    else:
        reply = "すみません、よく分かりませんでした。"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)