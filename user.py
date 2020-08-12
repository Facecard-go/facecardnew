import pymysql

def tuijian(user_id): # 要查询的用户id
    conn = pymysql.connect(host='139.219.8.186',
                           port=3306,
                           user='root',
                           password='123456',
                           database='facecard',
                           charset="utf8")
    purchase_records = {}  # 定义该用户购买不同类型商品空字典
    jifen = 0#定义积分为0
    cls = conn.cursor()
    cls.execute("SELECT * FROM facecard")
    hang = cls.fetchall()#获取总行数元组
    for i in range(1,100):  # 遍历所有行
        cls.execute("select * from facecard where uid=%s", [i])
        result = cls.fetchone()
        if str(result[1]) == user_id:  # 判断第1列是否为要查询的用户id
            jifen = jifen+10#每一条记录对应10积分
            if result[5] not in purchase_records:
                purchase_records[result[5]] = 1  # 在商品类型字典中创建一个新的类型并添加一次购买记录
                continue
            if result[5] in purchase_records:
                purchase_records[result[5]] = purchase_records[result[5]] + 1  # 在商品类型字典该种类添加一次购买记录
                continue

    descending_order = sorted(purchase_records.items(), key=lambda x: x[1], reverse=True)# 购买商品数量降序字典

    recommend = []  # 定义推荐空列表
    if len(descending_order) == 0:#无购买记录
        return "啊哦——该用户没有个性化推荐"
    else:# 存在购买记录，可以进行智能推荐
        if len(descending_order) == 1:
            recommend.append(descending_order[0][0])
            fanhui = "为该用户推荐的商品类别id为：" + str(recommend[0])

        if len(descending_order) == 2:
            recommend.append(descending_order[0][0])
            recommend.append(descending_order[1][0])
            fanhui = "为该用户推荐的商品类别id为：" + str(recommend[0])+"、"+str(recommend[1])

        if len(descending_order) >= 3:# 当购买商品类型多于3种时，只为此用户推荐购买次数较多的前3种商品
            recommend.append(descending_order[0][0])
            recommend.append(descending_order[1][0])
            recommend.append(descending_order[2][0])
            fanhui = "为该用户推荐的商品类别id为：" + str(recommend[0])+"、"+str(recommend[1])+"、"+str(recommend[2])

        return str(fanhui+"\n该用户的积分为:"+str(jifen))
# print(tuijian("378753"))