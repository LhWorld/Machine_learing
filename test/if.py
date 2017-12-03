#coding:utf-8
# age = input("请输入年龄:")
# age =int(age)
# if age > 16 and age < 30:
#     if age < 20:
#         print('少年')
#     else:
#         print('青年人')


# 循环都要设定一个边界，否则就是死循环
# 在循环体中需要修改变量
# i = 0
# sum =0
# while  i <=100:
#     sum=sum+i
#     i+=1
# print(sum)


i =1
while i<10:
    j =0
    while j<i:
        j+=1
        print('%d * %d ='%(j,i),j*i,'\t',end='')
    print()
    i+=1