#coding:utf-8
class Person(object):
    address='beijing'

    # 定一个类函数，函数的第一个参数必须是当前的类
    @classmethod
    def test2(cls):
        print('类方法')

    # 定一个静态函数，函数的参数必不做限定. 通过类名来直接调用
    @staticmethod
    def test3():
        pass

    # 定义个对象的函数,函数第一个参数必须是self
    def test1(self,msg):
        print(msg)
        print(self.name)

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __del__(self):
        print('该对象内存被回收')

p =Person('zhangsan',45)
# p.test1('hello')
print(p.address)
p2=p
del(p)
print('--'*20)
Person.test2()
# Person.test1('hello') # 对象的函数不能通过类名来调用

a=(1,2)

def test4():
    pass