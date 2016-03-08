#encoding:utf-8
import MySQLdb
#连接数据库api
f=open('acticoder.txt','r')
conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
curs=conn.cursor()
try:
    conn.query("CREATE DATABASE code")
    conn.query("GRANT ALL ON code.* to ''@'localhost'")
except Exception:
    print 'DATABASE code exists'
conn.select_db('code')

try:
    curs.execute('drop table activatecoder')
    curs.execute('CREATE TABLE activatecoder(coder char(64))')
except Exception:
    print 'table activatecoder has existed'
for line in f:
    curs.execute("INSERT INTO activatecoder VALUES (%s)",line )
curs.execute('select * from activatecoder')
curs.close()
conn.commit()
conn.close()





