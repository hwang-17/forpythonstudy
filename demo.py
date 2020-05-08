'''
编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）
题目来自 小甲鱼 python零基础 19课
'''


# 第一种方法
# def roundwords(string):
#     wordlength = len(string)
#     lastindex =wordlength-1
#     wordlength//=2
#     flag =1
#     for i in range(wordlength):
#         if string[i] !=string[lastindex]:
#             # 只要有不一样的字母， flag就会变成0. 否则， 就一直是之前定义的1
#             flag=0
#         lastindex=lastindex-1
#
#     if flag==1:
#         return  1
#     else:
#         return 0
#
# string=input("please input something:")
# if roundwords(string)==1:
#     print("roundword")
# else:
#     print("not roundword")



# 第二种方法

def roundwords(string):
    list1=list(string)
    list2=reversed(list1)
    注意reversed返回的是一个对象，我们需要把它转换成相应的变量， 这里用list转变。
    if list1==list(list2):
        return "roundword"
    else:
        return "not roundword"

string= input("please input something:")

print(roundwords(string))
