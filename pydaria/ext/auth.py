# from flask_simplelogin import SimpleLogin, login_required

# def verify_login(user):
#     return user.get('username') == 'admin' and user.get('password') == '12345'

# def init_app(app):
#     SimpleLogin(app, login_checker=verify_login)


from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from ext.database import db
from models import User


def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def verify_login2(user):
    return user.get('username')=='admin' and user.get('password')=='12345'


def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} ja esta cadastrado')
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login2)