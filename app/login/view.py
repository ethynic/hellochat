from flask import render_template,request,url_for,redirect,flash,make_response,session
from app.loginForm import LoginForm as Form
from flask_login import login_user
from . import login
from ..models import User


@login.route('/login',methods = ['GET', 'POST'])
def login_in():
    if session:
        return redirect(url_for('static',filename='index.html'))
    else:
        form = Form()
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.name.data).first()
            if user is not None and user.vefiy_password(form.password.data):
                login_user(user)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('static',filename='index.html')
                    resp = make_response(redirect(next))
                    resp.set_cookie('user_id',str(user.id))
                    resp.set_cookie('user_name',user.username)
                    return resp
            flash('用户名或者密码不正确')
        return render_template('login.html',loginform=form)