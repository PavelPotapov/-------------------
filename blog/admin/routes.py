from .admin import admin
from ..models import *
from run import app, db
from flask import flash, make_response, render_template, request, session, g, current_app, url_for, redirect
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

#функция проверки авторизации пользователя(админа)
def is_auth():
    if bool(request.cookies.get('is_admin_auth')):
        return True
    else:
        if 'is_admin_auth' in session:
            if session['is_admin_auth'] == True:
                    return True
            else:
                return False
        else:
            return False


@admin.route('/')
def index():
    return render_template('admin/login.html')


#обработчик логина
@admin.route('/login_auth', methods=['POST'])
def login_auth():
    login = request.form.get('login')
    password = request.form.get('password')
    remember = request.form.get('remember')
    user = db.session.query(Admin).filter_by(login=login).first()
    if user:
        if check_password_hash(user.password,password):
            g.current_user = user
            session['is_auth'] = True
            session['login'] = g.current_user.login
            session['surname'] = g.current_user.secondname
            if remember:
                res = make_response(render_template('profile.html', data=g.current_user))
                res.set_cookie('is_auth', 'True', max_age=60*60*24)
                res.set_cookie('login', login, max_age=60*60*24)
                return res
            else:
                return render_template('profile.html', data=g.current_user)

    else:
        flash('Неверный логин или пароль')
        return render_template('login.html')


#страница профиля
@admin.route('/profile')
def profile():
    if is_auth():
        g.current_user = db.session.query(Admin).filter_by(login=session['login']).first()
        return render_template('profile.html', data=g.current_user)
    else:
        return 'не авторизован!'

@admin.route('/userava')
def userava():
    if is_auth():
        g.current_user = db.session.query(Admin).filter_by(login=session['login']).first()
        img = g.current_user.avatar
        if not img:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), 'rb') as f:
                    img = f.read()
            except:
                print("файл не найден!")

        h = make_response(img)
        h.headers['Content-Type'] = 'image/png'
        return h
    return ''

@admin.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                img = file.read()
                i = db.session.query(Admin).filter_by(login=session['login']).first()
                i.avatar = img
                db.session.add(i)
                db.session.commit()
                #user_setting = db.session.query(User).filter_by(login=current_user.login).update(avatar=img)
                #db.session.commit()
            except:
                flash('Произошла ошибка загрузки файла на сервер')
    
    return redirect('profile')


