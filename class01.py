# 类

#普通方法
def ccc():
    print("123321456")

#类包含了属性（特征）和方法（行为，能干啥）
class Person():
    
    #成员变量，无论哪个地方都能使用成员变量
    name = "王五"
    age = 18
    high = 170
    xb = "男"

    #成员方法，以self参数开头的方法
    def chang(self):
        print("大家好，我是练习生")
        print("还有跳")
        print("还有篮球")

    #成员方法的传参
    def tiao(self,wd):     #wd = "广场舞"
        print("我会跳{}".format(wd))

    #self的用法
    #self和实例化对象一样，self在类里面用，实例化对象在外面，/
     #简单的说就是self在类的内部代指类自己，实例化类在外部表示类/就是
       # 说，成员方法，就是在类里面要引用就是用self指代，在类外面用的时候，
        # 直接用定义的实例化去指代呀。

    def rap(self):
        a = self.name  
        print(a)

#实例化类：p是person的实例化对象
#应用类，不要放到类的里面去
d = Person()    #赋值语句
print(d.name)   #引用类的成员变量
d.chang()        #引用类的成员方法
d.tiao("广场舞")  #成员方法的传参

d.rap()          #self在类里面引用变量和方法 


