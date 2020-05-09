"""
该代码为小甲鱼教程递归课堂练习。Python零基础P24 Fibonacci
"""


# 方法一：迭代的方法
#
# def fab(n):
#     tu1=1
#     tu2=1
#     tu3=1
#     if n<1:
#         print("wrong inputs")
#         return -1
#
#     while (n-2)>0:
#         tu3=tu2+tu1
#         tu1=tu2
#         tu2=tu3
#         n=n-1
#
#     return tu3
#
# result = fab(20)
#
# if result!=-1:
#     print("there are %d Tuzi" %(result))

# 第二种方法递归
def fab(n):
    if n<1:
        print("wrong inputs")
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

result=fab(20)
if result !=-1:
    print("there are %d  Tuzi in total" %(result))

