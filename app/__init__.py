# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# db = SQLAlchemy(app)
# app.config.from_object('config')
# from app import views
# from app import views, models
# import os
# from flask_login import LoginManager
# from flask_openid import OpenID
# from config import basedir
# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
# import os
# from flask_login import LoginManager
# from flask_openid import OpenID
# from config import basedir
# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))