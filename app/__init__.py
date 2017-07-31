# -*- coding:utf-8 -*-
__author__ = 'xuan'

from flask import Flask,session
from flask.ext.mail import Mail
from config import  config
from flask_admin import Admin
from flask_login import logout_user,login_required,login_user,current_user
from flask.ext.moment import  Moment


import os.path as op
from flask_babelex import Babel  #在本地上这里有用flask_babelex 服务器上用flask_babel ？
from models import db,User,login_manager


mail = Mail()
moment = Moment()

# my_admin = Admin(name='Admin',template_mode='bootstrap3',
#                                     index_view=AdminIndexView(
#                                     template='admin/custom.html',
#                                     url='/admin'
#                                     ))


# my_admin.add_view(UserModelView(db.session,name=u"用户",category='Models'))
# my_admin.add_view(PerformModelView(db.session,name=u"绩效",category='Models'))
# my_admin.add_view(ClientModelView(db.session,name=u"客户管理",category='Models'))


# models_list = [Role, User]
# for model in models_list:
#     my_admin.add_view(CustomModelView(model, db.session, category='Models'))   

def create_app(config_name):
    app = Flask(__name__)
    app.debug = False
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        override = 'zh_CN'
        if override:
             session['lang'] = override
        return session.get('lang', 'en')

    from .views.account import  auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .views.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
