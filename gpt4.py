from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
chat_api_url = "http://142.171.77.186:7077/api/chat/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 从请求中获取JSON数据
        data = request.get_json()

        # 提取必要的参数
        channel_id = data.get("channelID")
        stream = data.get("stream")
        content = data.get("content")

        # 构建聊天接口请求数据
        chat_data = {
            "channelID": channel_id,
            "stream": stream,
            "content": content
        }

        # 发送请求到聊天接口
        response = requests.post(chat_api_url, json=chat_data)

        # 获取聊天接口的响应并返回
        if response.status_code == 200:
            chat_response = response.json()
            return jsonify(chat_response)
        else:
            return jsonify({"error": "Chat API request failed"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5777)