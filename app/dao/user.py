# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from app.core.db import db
from app.models.user import User


class UserDao:
    # 获取用户列表
    @staticmethod
    def get_user_list(page, size):

        return {"total": 2, "current_page": 3, "items": 5}
    @staticmethod
    def create_user(form):
        with db.auto_commit():
            user = User.create(
                commit=False,
                nickname=getattr(form, 'nickname', None),
            )
        
