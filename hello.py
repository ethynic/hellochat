from flask import Flask,request,make_response,render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
openai.api_key = "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"
# 允许跨域
CORS(app)

@app.route("/")
def init_app():
    return render_template('index.html')


@app.route("/anwser",methods = ["POST"])
def anwser():
    question = request.get_json().get('question')
    if question :
        res = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"system","content":"你是程序员的好帮手，帮助程序员找到示例代码，解决复杂的技术问题！"},
                {"role":"user","content":f"{question}"}
                ]
        )
        response = make_response(res)
        # response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    
# @app.route("/anwser",methods = ["OPTIONS"])
# def options():
#     response = make_response()
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "POST"
#     response.headers["Access-Control-Allow-Headers"] = "Content-Type"
#     return response
