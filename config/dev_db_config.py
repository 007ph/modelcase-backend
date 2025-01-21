# _*_ coding: utf-8 _*_
"""开发环境配置文件"""
import os

# 数据库配置
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "../app.sqlite3")
SQLALCHEMY_TRACK_MODIFICATIONS = False
