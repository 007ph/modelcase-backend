# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
  ↓↓↓ 普通用户接口 ↓↓↓
"""
from flask import Blueprint


from app.models.user import User
from app.dao.user import UserDao
from app.core.error import Success

api = Blueprint("v1_user", __name__)


@api.route("/user", methods=["GET"])
def get_user():
    """查询自身"""
    user = User.get(id=1)
    return user
