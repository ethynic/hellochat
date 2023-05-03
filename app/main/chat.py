from flask import request,make_response,render_template,current_app,redirect,url_for
import openai
from . import main
from flask_cors import cross_origin
from app.loginForm import LoginForm as Form


openai.api_key = "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"
# openai.api_key = current_app.config['OPEN_AI_KEY']


@main.route("/")
@cross_origin()
def index():
    return redirect(url_for('login.login_in'))
    
    
@main.route("/anwser",methods = ["POST"])
@cross_origin()
def anwser():
    question = request.get_json().get('question')

    if question :
        if len(question) > 10:
            question = question[-10:]
        res = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            # messages = [
            #     {"role":"system","content":"你是程序员的好帮手，帮助程序员找到示例代码，解决复杂的技术问题！"},
            #     {"role":"user","content":f"{question}"}
            #     ]
            messages = question
        )
        response = make_response(res)
        # response.headers["Access-Control-Allow-Origin"] = "*"
        return response