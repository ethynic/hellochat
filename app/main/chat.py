from flask import request,make_response,render_template,current_app
import openai
from . import main
from flask_cors import cross_origin


openai.api_key = "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"
# openai.api_key = current_app.config['OPEN_AI_KEY']

@main.route("/")
@cross_origin()
def index():
    if request.cookies.get('name') == None:
        return render_template('login.html')
    current_app.send_static_file('index.html')
    
    

@main.route("/anwser",methods = ["POST"])
@cross_origin()
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