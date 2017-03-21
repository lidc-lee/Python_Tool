# coding=utf-8

"""
@company:广东浩迪创新科技有限公司
@version: ??
@author: AA-ldc
@file: testDB.py
@time: 2017/3/20 9:24
@function：数据库的操作
"""
import pymssql


class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


def main():
    # ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
    # #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    # ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL(host="localhost:1433", user='sa', pwd='123456', db="test")
    resList = ms.ExecQuery("SELECT name FROM person")
    for (name) in resList:
        print str(name).decode("utf8")

if __name__ == '__main__':
    main()
