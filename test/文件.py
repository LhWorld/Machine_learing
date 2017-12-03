#coding:utf-8

# f = open('data.txt','w+')
# f.write('hello world, i am here!')
# f.close()

# result = f.read() # read没有传参，读取整个文件 ,read没有返回结果，则文件已经读完

f =open(r'd:\22.jpg','rb')
new_f =open(r"d:\\666.jpg",'wb')
data = f.read(1024)
while data:
    new_f.write(data)
    data=f.read(1024)
new_f.close()
f.close()