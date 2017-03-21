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

    def Commit(self):
        self.conn.commit()

    def Roolback(self):
        self.conn.rollback()

    def CreatTab(self):
        sql = """CREATE TABLE LWL(
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        cur = self.__GetConnect()
        # 如果数据表已经存在使用 execute() 方法删除表。
        # cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
        try:
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # Rollback in case there is any error
            self.conn.rollback()

        self.conn.close()

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

        # # 查询完毕后必须关闭连接
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

    def Insert(self):
        sql = """INSERT INTO Stu(FIRST_NAME,
                     LAST_NAME, AGE, SEX, INCOME)
                     VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        cur = self.__GetConnect()
        try:
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # Rollback in case there is any error
            self.conn.rollback()

        # 关闭数据库连接
        self.conn.close()

def main():
    # ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
    # #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    # ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL(host="localhost:1433", user='sa', pwd='123456', db="test")
    resList = ms.ExecQuery("SELECT name FROM person")
    for (name) in resList:
        print str(name).decode("utf8")

    ms.CreatTab()
    ms.Insert()
    resList = ms.ExecQuery("SELECT * FROM Stu")
    for (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) in resList:
        print str(FIRST_NAME).decode("utf8")
        print int(AGE)

if __name__ == '__main__':
    main()
