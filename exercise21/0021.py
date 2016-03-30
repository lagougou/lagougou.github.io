from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import hashlib

import sqlite3
conn=sqlite3.connect('test.db')
cusor=conn.cursor()




def create():
    cusor.execute('create table user(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(20),pwd VARCHAR (20))')
    conn.commit()

def set_password(password):
    sha256=hashlib.sha256()
    sha256.update(password)
    return repr(sha256.hexdigest())

def register():
    username=raw_input('your username:')
    password=raw_input('your password:')
    names=query()
    while True:
        if username in names:
            print 'the username has exsited,please retype your username >>>'
            username=raw_input('your username:')
            password=raw_input('your password:')
        break
    password=set_password(password)
    t=(username,password)
    cusor.execute('insert into user (name,pwd) VALUES (?,?)',t)
    conn.commit()

def login():
    name=raw_input('your name:')
    password1=raw_input('your password:')
    password1=set_password(password1)
    cusor.execute('select pwd from user where name=?',[name])
    password=cusor.fetchone()

    if password!=None:
        if password1==''.join(password):
            print 'Welcome to our world!'
        else:
            print 'incorrect password'
    else:
        print 'incorrect username!'

def query():
    names=[]
    cusor.execute('select *from user')
    for each in cusor.fetchall():
        names.append(each[1])
    return  names

def main():
    cmd=raw_input('type the command your want "(register or login)"')
    if cmd==register.func_name:
        try:
            create()
        except sqlite3.OperationalError ,e:
            print(e)
            register()
    elif cmd==login.func_name:
        login()

    else:
        print 'command incorrect'
    cusor.close()
    conn.commit()
    conn.close()

if __name__=='__main__':
    main()









