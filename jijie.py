import pymysql
import time #时间数据分析
'''
本模块为季节的搜索功能的后端代码，实现数据处理
author:刘益争
create date:2020-8-4
update date:2020-8-10
'''
def jijie(cateloge_id):#要查询的商品种类代码
    conn = pymysql.connect(host='139.219.8.186',
                           port=3306,
                           user='root',
                           password='123456',
                           database='facecard',
                           charset="utf8")
    first_quarter = 0
    second_quarter = 0
    third_quarter = 0
    fourth_quarter = 0
    cls = conn.cursor()
    cls.execute("SELECT * FROM facecard")
    hang = cls.fetchall()  # 获取总行数元组
    for i in range(1,100):#遍历所有行
        cls.execute("select * from facecard where uid=%s", [i])
        result = cls.fetchone()
        if str(result[5]) == cateloge_id:
            datatime = result[6]#日期时间数据依次读取
            yuanzu = time.strptime(str(datatime), '%Y%m%d%H%M%S')  # 字符串转时间元组
            month = time.strftime("%m", yuanzu)  # 时间元组可视化，即将月份读给month
            if int(month) <= 3:#按照季度累计该种类商品销量
                first_quarter = first_quarter+1
                continue
            if int(month) >= 4 and int(month) <= 6:
                second_quarter = second_quarter+1
                continue
            if int(month) >= 7 and int(month) <= 9:
                third_quarter = third_quarter+1
                continue
            if int(month) >= 10 and int(month) <= 12:
                fourth_quarter = fourth_quarter+1
                continue
    sales_volumes = [first_quarter, second_quarter, third_quarter,fourth_quarter]  #某一季度某一种类商品销售数量列表
    return sales_volumes
