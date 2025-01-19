from flask import g, request, current_app

from app.core.db import EntityModel, db


class User(EntityModel):
    """用户"""
    
    __tablename__ = "user"

    serialize_rules = ("-id", "-group_id")

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(24), comment="昵称")
    group_id = db.Column(db.Integer, comment="用户所属的权限组id")
    _avatar = db.Column("avatar", db.String(255), comment="头像url")
    extend = db.Column(db.String(255), comment="额外备注")

    def __repr__(self):
        return f"<User(id={self.id}, nickname={self.nickname})>"

    @property
    def avatar(self):
        if self._avatar is not None:
            host_url = request.host_url
            host_url = host_url.split(",")[-1] if "," in host_url else host_url
            host_url = host_url[:-1]  # 当前host的路径 http://192.168.10.80:8010
            static_url_path = (
                current_app.static_url_path[1:] + "/avatars"
            )  # static/avatars
            return "{0}/{1}/{2}".format(host_url, static_url_path, self._avatar)
        return self._avatar

    @classmethod
    def get_current_user(cls):
        """获取当前用户"""
        return g.user
