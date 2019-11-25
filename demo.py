'''
xx = [1,7,"哈哈","嘻嘻",50,(2,3,4,6)]
xx.append(66)
print(xx)
xx.insert(1,"腾讯")
print(xx)
yy = xx.pop(3)
print(yy)



xx= {
    "姓名":"张三",
    "年龄":28,
    "籍贯":"北京"
    }
print(xx["籍贯"])



xx = [1,7,"哈哈","嘻嘻","呜呜",50,(2,3,4,6)]
print(xx[2]) 
'''



# 字典新增
# xx = {0:"张三",1:"李四",2:"王五"}
# xx["age"] = 20
# print(xx)


# 字典删除
# xx = {0:"张三",1:"李四",2:"王五"}
# del xx[2]
# print(xx)



'''
二元取值

xx = {
    0:"张三",
    1:"李四",
    2:"王五",
    "元组":(1,2,3,4),
    "数组":["哈哈","嘻嘻","呜呜"]
    }

a = xx["数组"][0]    
print(a) 

'''


# 二元二次数组取值
# 
# yy = [1,2,3,4,["哈哈","嘻嘻","嘿嘿"]]
# b = yy[4][2]
# print(b)


# 
# 批量取值只能取某个区间的值
# yy[0:4] 表示取从第0个到第4个值，但不包含第4个值
# 这就是左闭右开法则
# 
# yy = [1,2,3,4,["哈哈","嘻嘻","嘿嘿"]]
# print(yy[0:4])
  
# print(yy[:4]) 也是一样的，默认从第0个值开始，到第4个值



'''
# len用来表示一共有多少值

yy = [1,2,3,4,["哈哈","嘻嘻","嘿嘿"]]
xx = {
    0:"张三",
    1:"李四",
    2:"王五",
    "元组":(1,2,3,4),
    "数组":["哈哈","嘻嘻","呜呜"]
    }
print(len(xx))
print(len(yy))

'''



# # 字符串于数组的转换

# hstr = "我的法克问佛看姑婆玩个屁"
#  print(list(hstr))
#  print(hstr[0])
# 


'''
format的用法
 
x = 25
print("大家好，我今年{}岁".format(x))
 
name = input("请输入你的名字：") 
aihao = input("请输入你的爱好：")
job = input("请输入你的职业；")
print("大家好,我叫{name},我是{job},我的爱好是{aihao},做{job}很有\
    趣".format(name=name,aihao=aihao,job=job))

'''






# age = int(input("请输入你的年龄:"))
# if age > 25:
#     print("人生百态")
# elif age > 18:
#     print("大学的美好时光")   
# elif age > 12:
#     print("不要早恋")
# else:
#     print("你还小")        


# age = 18
# if type(age) is int:
#     print("age的类型是int")
# elif type(age) is str:
#     print("age的类型是str")
# else:
#     print("其他")
 
 

# hlist = ["哈哈","嘻嘻","你好","张三"]
# for i in hlist:
#     print(i)
 


# hstr = "fesf905gerwfewf94gwq"
# num = 0
# for i in hstr:
#     num = num + 1
# print(num) 
# print(len(hstr))




'''
money = input("请输入红包的金额:")
for i in money:
    if i not in "0123456789.":
        print("输入的值不合法，请输入数字")
        exit()
xx = money.count(".")
if xx > 1:
    print("输入的值不合法！")
else: 
    if "." in money:
        yy = money.index(".") + 1
        zz = len(money)
        floatlen = zz - yy
        if floatlen > 2:
            print("只能有两位小数")
        else:
            money = float(money)
            if money >= 0.01 and money <= 200:
                print("发送红包成功,金额{}".format(money))
            else:
                print("发送红包失败，{}不在范围内".format(money))   

    else:   
        money = float(money)
        if money >= 0.01 and money <= 200:
            print("发送红包成功,金额{}".format(money))
        else:
            print("发送红包失败，{}不在范围内".format(money))   

    

 '''



#  for循环

# a = [2,0,3,1,4,25,36,66,70]
# for i in a:
#     if i == 4:  #  "=="是用来判断i是否等于4的，一般if和while右边都要用"=="
#         break
#     print(i)



#　ｗhile循环

# a = [1,2,3,4,5,6,7,8,9]
# i = 0
# while i < len(a):
#     i = i +1
#     print(i)




a = ["哈哈",1,4,25,"你好",36,66,"jsdf",70]
for i in a:
    if type(i) is not int and type(i) is not float:
        continue
    print(i)








