import pymysql
def connect():
    conn=pymysql.connect(host='127.0.0.1',user="root",password='',database='tolltaxdb')
    # conn=pymysql.connect(host='13.232.35.56',user="anisha",password='anisha@123',database='anisha')

    return conn