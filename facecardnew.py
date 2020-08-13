'''
本模块为项目路由，包含部分功能实现
author:淘卡团队（详细分工下文有注释）
create date:2020-7-28
update date:2020-8-13
'''
from flask import Flask,render_template,request,flash,Response
import  pymysql
import read_camera
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from gevent.pywsgi import WSGIServer
import time
import cv2
import sys
import os
from train_model import Model
from read_data import read_name_list
import time #时间数据分析
import jijie
import exercise
import user
from flask import jsonify
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
'''
本模块实现登录功能
author:原也
create date:2020-7-29
update date:2020-8-9
'''
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

'''
本模块实现注册功能
author:原也
create date:2020-7-29
update date:2020-8-9
'''
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
#################################################人脸识别################################################
'''
本模块实现人脸识别功能
author:许如昕
create date:2020-8-1
update date:2020-8-10
'''

# face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_frontalface_alt2.xml')   # 正脸模型

class Camera_reader(object):
    #在初始化camera的时候建立模型，并加载已经训练好的模型
    def __init__(self):
        self.model = Model()
        self.model.load()
        self.img_size = 128


    def build_camera(self):
        #opencv文件中人脸级联文件的位置，用于帮助识别图像或者视频流中的人脸
        face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_frontalface_alt2.xml')
        #读取dataset数据集下的子文件夹名称
        name_list = read_name_list(r'E:\cut-face')

        #打开摄像头并开始读取画面
        cameraCapture = cv2.VideoCapture(0)
        success, frame = cameraCapture.read()

        while success and cv2.waitKey(1) == -1:
             success, frame = cameraCapture.read()
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #图像灰化
             faces = face_cascade.detectMultiScale(gray, 1.3, 5) #识别人脸
             for (x, y, w, h) in faces:
                 ROI = gray[x:x + w, y:y + h]
                 ROI = cv2.resize(ROI, (self.img_size, self.img_size), interpolation=cv2.INTER_LINEAR)
                 label,prob = self.model.predict(ROI)  #利用模型对cv2识别出的人脸进行比对
                 if prob >0.7:    #如果模型认为概率高于70%则显示为模型中已有的label
                     show_name = name_list[label]
                 else:
                     show_name = 'Stranger'
                 cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  #显示label
                 frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  #在人脸区域画一个正方形
                 # name_id = show_name
             cv2.imshow("Camera", frame)

        cameraCapture.release()
        cv2.destroyAllWindows()
        return(show_name)
        # return(show_name)   #返回识别的人脸id

@app.route('/face')  # 进入人脸识别页面
def face():
    # show_name = camera.build_camera()
    return render_template('face.html')

def gen(camera):
    while True:
        frame=camera.build_camera()
            # 使用generator函数输出视频流， 每次请求输出的类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')  # 返回视频流响应
def video_feed():
    return Response(gen(Camera_reader()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

######################################人脸识别有关part结束~~######################################################
'''
本模块实现展示进货列表功能
author:高万崧
create date:2020-8-3
update date:2020-8-9
'''
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
'''
进货列表结束
'''

@app.route('/changxiao')
def changxiao():
    return render_template("changxiao.html")

@app.route("/shouzhong")
def shouzhong():
    return render_template("shouzhong.html")

@app.route("/guest")
def guest():
    return render_template("guest.html")
'''
本模块实现畅销页面的前后端交互
author:原也
create date:2020-8-5
update date:2020-8-12
'''
@app.route('/show2',methods=['get','post'])
def showCX():
    print("hello_CX")
    catelogeid = request.values.get("xiao")
    result1 = exercise.xiaoliang(catelogeid)[0]
    result2 = exercise.xiaoliang(catelogeid)[1]
    print("catelogeid:%s"%(catelogeid))
    print("result1:%s,result2:%s"%(result1,result2))
    return jsonify({"bb":result1,"cc":result2})
    # return render_template("line-simple.html",x=result1,y=result2,z=type(result1_json))
'''
本模块实现季节页面的前后端交互
author:原也
create date:2020-8-5
update date:2020-8-12
'''
@app.route('/show1',methods=['get','post'])
def showJijie():
    cateloge_id=request.values.get("abc")
    jijie_tu=jijie.jijie(cateloge_id)
    print("cateloge_id:%s" % (cateloge_id))
    print("jijie_tu:%s"%jijie_tu)
    return jsonify({"aa":jijie_tu})
'''
本模块实现帮助文档页面跳转
author:原也
create date:2020-8-4
update date:2020-8-11
'''
@app.route('/help',methods=['get','post'])
def help():
    return render_template("help.html")
'''
本模块实现顾客页面的前后端交互
author:刘益争
create date:2020-8-5
update date:2020-8-13
'''
@app.route('/showuser',methods=['get','post'])
def showuser():
    user_id=request.values.get("user_id")
    return  user.tuijian(user_id)

if __name__ == '__main__':
    app.run()
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    print("* Running on http://127.0.0.1:5000/ ")
    http_server.serve_forever()
