__author__ = 'miles'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
from config import mysql_m2cchinaerp_prd as mysql_config

MYSQL_USER = mysql_config["MYSQL_USER"]
MYSQL_SERVER = mysql_config["MYSQL_SERVER"]
MYSQL_PASSWORD = mysql_config["MYSQL_PASSWORD"]
MYSQL_DB = mysql_config["MYSQL_DB"]
MYSQL_PORT = mysql_config["MYSQL_PORT"]

def get_mysql_conn(mysql_user, mysql_server, mysql_password, mysql_db, mysql_port):
    try:
        mysql_conn = MySQLdb.connect(user=mysql_user,
                  charset = 'utf8',
                  host = mysql_server,
                  passwd = mysql_password,
                  db = mysql_db,
                  port = mysql_port)
        return mysql_conn
    except Exception, e:
        ERROR_HINT = " [ get mysql connection failed ] MYSQL_USER:"+mysql_user+", MYSQL_SERVER:"+mysql_server+", MYSQL_DB:"+mysql_db
        print ERROR_HINT
        print e
        return None


def get_store_info_by_id(comp_id):
    print "start...get_store_info_by_id"
    conn = get_mysql_conn(MYSQL_USER, MYSQL_SERVER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_PORT)
    curr = conn.cursor()
    sql = """
      select `comp_id`, `store_name`, `store_name_cn`, `subdomain`, `contact`, `email`, `tel`, `status`
      from `store$company`
      where 1 = 1
    """
    if comp_id and comp_id > 0:
        sql = sql + """ and comp_id =  """ + comp_id
    curr.execute(sql)
    mysql_rs = curr.fetchall()
    data = []
    for rs in mysql_rs:
        data_temp = {}
        try:
            data_temp["comp_id"] = rs[0]
            data_temp["store_name"] = rs[1]
            data_temp["store_name_cn"] = rs[2]
            data_temp["subdomain"] = rs[3]
            data_temp["contact"] = rs[4]
            # data_temp["contact"] = str(rs[4].encode('utf-8'))
            data_temp["email"] = rs[5]
            data_temp["tel"] = rs[6]
            data_temp["status"] = rs[7]
            data.append(data_temp)
        except Exception, e:
            print data_temp
            print e
            break
    curr.close()
    curr.close()
    print "end...get_store_info_by_id"
    return data