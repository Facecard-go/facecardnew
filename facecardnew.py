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
# app = Flask(__name__)
currPath = sys.path[0]
app = Flask(__name__, template_folder=currPath+'\\templates')
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

#人脸识别部分
#人脸识别模型
# face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_frontalface_default.xml') # 默认模型
# face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_profileface.xml')         # 侧脸模型
face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_frontalface_alt2.xml')   # 正脸模型

#如果文件不存在则创建
if not os.path.exists('facesData'):
    os.makedirs('facesData')
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        # try:
        faces = face_cascade.detectMultiScale(image, 1.3, 5)
        for (x, y, w, h) in faces:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # cv2.imwrite("facesData/"+str(time.time())[:10]+ ".jpg", image[y-40:y+h+40, x-20:x+w+20])
            cv2.imwrite("facesData/" + str(time.time())[:10] + ".jpg", gray[y - 40:y + h + 40, x - 20:x + w + 20])

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.waitKey(100)

        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


@app.route('/face')  # 进入人脸识别页面
def face():
    # 具体格式保存在index.html文件中
    return render_template('face.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/getGoodList')
# 获取商品列表
def getGoodsList():
    # 商品列表
    goodsList = []
    user = {'name': 'Miguel', 'url': '', 'img': '', 'money': ''}
    goodsList.append(user)
    return goodsList

@app.route('/jinhuo')
def show_index():

    #网页标题
    title = '进货列表'

    #获取商品列表
    goodsList = getGoodsList()

    return render_template('jinhuo.html', title=title, list=goodsList)

@app.route('/changxiao')
def changxiao():
    return render_template("changxiao.html")

@app.route("/shouzhong")
def shouzhong():
    return render_template("shouzhong.html")

@app.route("/guest")
def guest():
    return render_template("guest.html")

if __name__ == '__main__':
    app.run()
