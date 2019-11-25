import pymysql  #导入数据库
'''
1连接数据库
2选择数据库
3获取游标
4增删改查

'''
# def query(sql):
#     '''
#     这是数据库的查询方法 query是查询的意思，curso是游标的意思
#     '''
#     db = pymysql.connect(host="localhost",user="root",password="123456",db="textdb") #连接并选择数据库
#     cursor = db.cursor()    #获取游标
#     try:
#         cursor.execute(sql)  #执行sql语句
#         res = cursor.fetchall()    #获得查询结果
#         db.close()         #关闭数据库连接
#         return res
#     except:
#         return "SQL语句错误！请检查后再输入"

# a = query("select * from tt_grade")
# chlist = []
# for i in a:
#     chlist.append(i[2])
# print(chlist)

def commit(sql): 
    '''
    这是数据库的修改方法  commit相当于提交命令
    '''
    db = pymysql.connect(host="localhost",user="root",password="123456",db="textdb") #连接并选择数据库
    cursor = db.cursor()    #获取游标
    try:
        cursor.execute(sql)  #执行sql语句
        db.commit()        #应用改变
        db.close()         #关闭数据库连接
        return True
    except:
        return "SQL语句错误！请检查后再输入"
   

x = commit("insert into tt_class (id,cname) values (5,'张三');")
print(x)


 
# def function():
#     print("this is a function")
# function()

# def count(value):
#     xx = [1,2,3,4,5,5,5,6]
#     y = 0
#     for i in xx:
#         if i == value:
#             y = y + 1
#     print(y)

# count(5) 