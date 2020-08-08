from flask import Flask,render_template,request,flash,Response
import  pymysql
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import exercise
# import exercise1
from gevent.pywsgi import WSGIServer
import time
import cv2
import sys
import os
import time #时间数据分析
app = Flask(__name__)

@app.route('/',methods=['get','post'])
def moren():
    print("index")
    return render_template("index.html")
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/login_register')
def login_register():
    return render_template("login_register.html")
@app.route('/personal')
def personal():
    return render_template("personal.html")
@app.route('/season')
def season():
    return render_template("season.html")
@app.route('/spring')
def spring():
    return render_template("spring.html")
@app.route('/summer')
def summer():
    return render_template("summer.html")
@app.route('/autumn')
def autumn():
    return render_template("autumn.html")
@app.route('/winter')
def winter():
    return render_template("winter.html")
@app.route('/denglu',methods=['get','post'])
def denglu():
    print("hello_denglu")
    # 获取前端提交的用户名和密码
    uname = request.values.get("uname")
    password1 = request.values.get("password1")
    data=[uname,password1]
    print(data)
    # 到数据库中进行校验
    conn = pymysql.connect(
        host='139.219.8.186',
        port=3306,
        user='root',
        password='123456',
        database='facecard',
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    # 前端传递的数据，进行到数据库中进行验证
    cls.execute("select * from myuser where uname=%s and password1=%s",[uname,password1])
    result = cls.fetchone()
    if result is None:
        flash("user or password not true")
        return render_template("login_register.html")
    else:
        cls.execute("select * from myuser")
        result=cls.fetchall()
        conn.close()
        return render_template("personal.html",users=result)

#这里是连接虚拟机数据库的代码
@app.route("/zhuce" ,methods=["get","post"])
def zhuce():
    print("hello_zhuce")
# 连接mysql，括号内是服务器地址, 端口号, 用户名，密码，存放数据的数据库
    conn = pymysql.connect( host='139.219.8.186',
                        port=3306,
                        user='root',
                        password='123456',
                        database='facecard',
                        charset="utf8")
    cursor = conn.cursor() # Locate the Cursor, all that was required was for buffered to be set to true
    #获得表中有多少条数据
    uname=request.values.get("uname")
    email=request.values.get("email")
    password1=request.values.get("password1")
    password2=request.values.get("password2")
    cursor.execute("insert into myuser(uname,email,password1,password2)values(%s,%s,%s,%s)", [uname,email,password1,password2])
    print('ok')
    sqlcom="select * from myuser" # SQL command
    aa=cursor.execute(sqlcom) # Execute the command
    print(aa)
    #查询表中数据，并以每行一个元祖打印
    rows = cursor.fetchall() #使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
    #依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
    for a in rows:
        print(a)
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("login_register.html")




if __name__ == '__main__':
    app.run()
