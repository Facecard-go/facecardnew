
import inline as inline
import xlrd
import xlwt
import pandas as pd
import matplotlib.pyplot as plt
'''
本模块为受众分析，实现对顾客进行年龄和性别分析
author:武岳豪
create date:2020-8-7
update date:2020-8-10
'''
def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('../facecardnew/sj.csv')

    #按sheet名字获取sheet内容
    sheet1_content1 = workBook.sheet_by_name('Sheet1')

    # 3. sheet的名称，行数，列数
    #print(sheet1_content1.name,sheet1_content1.nrows,sheet1_content1.ncols);

    # 4. 获取整行和整列的值（数组）
    # rows = sheet1_content1.row_values(3); # 获取第四行内容
    cols = sheet1_content1.col_values(2) # 获取第三列内容
    cols = [int(i) for i in cols]
    print(cols)
    print(type(cols))

    re = [0,0,0]
    def all_list(cols):
        result = {}
        for i in set(cols):
            result[i] = cols.count(i)
        return result
    print(all_list(cols))
    def qsn(cols):
        for i in set(cols):
            for i in range(12,17):
                re[0] = re[0] + cols.count(i)
            return re[0]
    print(qsn(cols))
    def qn(cols):
        for i in set(cols):
            for i in range(18,45):
                re[1] = re[1] + cols.count(i)
            return re[1]
    print(qn(cols))
    def ln(cols):
        for i in set(cols):
            for i in range(46,69):
                re[2] = re[2] + cols.count(i)
            return re[2]
    print(ln(cols))
    print(re)

    df = {"人群":["青少年","青年","老年"],"数量":[qsn(cols),qn(cols), ln(cols)]}
    plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
    plt.pie(df['数量'], labels=df['人群'], explode=None, data=df, shadow=True, autopct='%1.1f%%')
    plt.title('Age segment percentage')
    plt.axis('equal')
    plt.show()
if __name__ == '__main__':
    read_excel()