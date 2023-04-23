from flask import render_template 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
from . import login


class LoginForm(FlaskForm):
    name = StringField('请输入用户名：',validators=[DataRequired()])
    password = PasswordField('请输入密码：',validators=[DataRequired()])
    submit = SubmitField('提交')



@login.route('/',methods = ['GET', 'POST'])
def login_in():
    form = LoginForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''
    return render_template('login.html',loginform=form)