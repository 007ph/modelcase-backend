import os
from flask import Flask
from flask_cors import CORS
from app.core.db import db
from flask import Flask
from app.core.redprint import register_redprints

IS_DEBUG = os.environ.get("FLASK_ENV") == "development"

def create_app(db_config="config.local_secure"):
    """创建 Flask 应用"""
    app = Flask(__name__)
    if IS_DEBUG:
        app.config.from_object(db_config)
        print("Running in development mode")
    else:
        app.config.from_pyfile(db_config)
        print(
            f"Running in production mode on {app.config.get('HOST')}:{app.config.get('PORT')}"
        )
    register_plugins(app)
    return app


def load_config(app: Flask, db_config_file):
    """加载配置"""

    if IS_DEBUG:
        app.config.from_object("config.local_secure")
        print(
            f"Running in development mode on {app.config.get('HOST')}:{app.config.get('PORT')}"
        )
    else:
        app.config.from_pyfile(db_config_file)
        print(
            f"Running in production mode on {app.config.get('HOST')}:{app.config.get('PORT')}"
        )
    app.config.from_object("config.setting")


def register_plugins(app: Flask):
    """注册插件"""
    register_redprints(app)
    register_db(app)
    register_cors(app)


def register_db(app: Flask):
    """连接数据库"""

    db.init_app(app)
    #  初始化使用
    with app.app_context():  # 手动将app推入栈
        db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表


def register_cors(app: Flask):
    """配置跨域"""

    cors = CORS()
    cors.init_app(app, resources={"/*": {"origins": "*"}})
