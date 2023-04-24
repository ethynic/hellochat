
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('请输入用户名：',validators=[DataRequired()],render_kw={'id':'username','placeholder':'请输入用户名：'})
    password = PasswordField('请输入密码：',validators=[DataRequired()],render_kw={'id':'password','placeholder':'请输入密码：'})
    remember_me = BooleanField('记住登录')
    submit = SubmitField('提交')
