from contextlib import contextmanager
from datetime import datetime


from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

from sqlalchemy_serializer import SerializerMixin # type: ignore


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()  # 事务
        except Exception as e:
            self.session.rollback()  # 回滚
            raise e


db = SQLAlchemy()


def on_update_time():
    now = datetime.now
    return int(round(now().timestamp()))


class CRUDMixin(db.Model,SerializerMixin):  # type: ignore
    """Mixin 添加CRUD操作: create, get(read), update, delete"""

    __abstract__ = True

    @classmethod
    def get(cls, **kwargs):
        """查询"""
        result = cls.query.filter_by(**kwargs).first()
        print(result)
        return result.to_dict() if result else None


class EntityModel(CRUDMixin):
    __abstract__ = True
    pass
