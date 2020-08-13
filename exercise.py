import pymysql
'''
本模块为畅销功能的数据分析
author:刘益争
create date:2020-8-2
update date:2020-8-11
'''
def xiaoliang(cateloge_id): # 要查询的商品类型代码
    conn = pymysql.connect(host='139.219.8.186',
                           port=3306,
                           user='root',
                           password='123456',
                           database='facecard',
                           charset="utf8")
    same_category_id = {}  # 定义同类型商品不同种类商品空字典
    cls = conn.cursor()
    cls.execute("SELECT * FROM facecard")
    hang = cls.fetchall()#获取总行数元组
    for i in range(1,100):  # 遍历所有行
        cls.execute("select * from facecard where uid=%s", [i])
        result = cls.fetchone()
        if str(result[5]) == cateloge_id:  # 判断第6列是否为要查询的商品类型
            if result[4] not in same_category_id:
                same_category_id[result[4]] = 1  # 在商品类型字典中创建一个新的种类并添加一次购买记录
                continue
            if result[4] in same_category_id:
                same_category_id[result[4]] = same_category_id[result[4]] + 1  # 在商品类型字典该种类添加一次购买记录
                continue

    descending_order = sorted(same_category_id.items(), key=lambda x: x[1], reverse=True)

    x = []  # 横坐标
    y = []  # 纵坐标
    for i in descending_order:  # 横纵坐标写入列表
        x.append(str(i[0]))
        y.append(i[1])
    fanhui = [x,y]

    return fanhui