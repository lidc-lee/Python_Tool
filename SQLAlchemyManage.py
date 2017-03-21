# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testDB.py
@time: 2017/3/20 9:24
@function：ORM--对象关系映射
"""

from sqlalchemy import exc, create_engine, orm
from contextlib import contextmanager
import ConfigParser
from data.User import Student


class SQLAlchemyManage(object):
    def __init__(self, db_name):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open('config/config.ini'), "rb")
            dsn = 'mssql+pymssql://%s:%s@%s/%s' % (config.get('mssql', 'user'), config.get('mssql', 'pwd'),
                                                   config.get('mssql', 'host'), db_name)
            eng = create_engine(dsn, echo=False)
        except ImportError:
            raise RuntimeError()
        try:
            eng.connect()
        except exc.OperationalError:
            raise RuntimeError()
        print ('Connect to database <%s> success.' % db_name)
        self.eng = eng

    def GetSession(self):
        # 定义会话类型
        SessionType = orm.scoped_session(orm.sessionmaker(bind=self.eng, expire_on_commit=False))
        return SessionType

    # 定义上下文函数，使能够自动进行事务处理，
    # 定义上下文件函数的方法就是加上contextmanager装饰器
    # 执行逻辑：在函数开始时建立数据库会话，此时会自动建立一个数据库事务；当发生异常时回滚（rollback）事务，当
    # 退出时关闭(close)连接
    @contextmanager
    def session_scope(self):
        session = self.GetSession()

        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise RuntimeError()
        finally:
            session.close()

    # 查询
    def Query(self):
        with self.session_scope() as session:
            users = session.query(Student).all()
            return users


def main():
    orm = SQLAlchemyManage("test")
    users = orm.Query()
    for user in users:
        print user.FIRST_NAME, user.AGE


if __name__ == '__main__':
    main()
