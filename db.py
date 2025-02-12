import pymysql

def get_db_connection():
    return pymysql.connect(
        host='mysql.sqlpub.com',
        user='miniprogram',
        password='EfNFKQuebqC8h2mT',
        database='mysql_cloud_database',
        cursorclass=pymysql.cursors.DictCursor
    )