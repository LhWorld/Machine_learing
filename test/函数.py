#coding:utf-8
# 默认值参数放到 **kwargs参数的前面
def test1(a,*m,b=1):
    print(a,b)
    print(type(m))
    print(m)
    # print(n['name'])

test1('hello',1,1,1)

a =100
def test2(b):
    global a
    a=300
    print(a)

test2(200)
print(a)

print([  [j*100+i  for i in range(100) ]  for j in range(100)])