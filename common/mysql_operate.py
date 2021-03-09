# coding = utf-8
import pymysql
import os
from common.logger import logger
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH,"config","setting.ini")
data = data.load_ini(data_file_path)["mysql"]
DB_CONF={
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB']
}

class MysqlDB():
    def __init__(self,db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(**db_conf,autocommit=True)
        # 通过cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    # 对象资源被释放时触发，在对象即将被删除时的最后操作
    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self,sql):
        """检查是否连接状态"""
        self.conn.ping(reconnect=True)

        # 执行sql
        self.cur.execute(sql)
        # 获取执行结果
        # data = self.cur.fetchall()
        data = self.cur.fetchone()
        return data

    def execute_db(self,sql):
        try:
            # 检查是否连接状态
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("操作mysql出现{}错误".format(e))
            self.conn.rollback()


db = MysqlDB(DB_CONF)