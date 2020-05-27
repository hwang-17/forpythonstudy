'''
1. 按照以下要求，定义一个类实现摄氏度到华氏度的转换
（转换公式：华氏度 = 摄氏度*1.8+32）zcZ"
this is practice is from fishc Forum
'''


class C2F(float):
    def __new__(cls, arg=0.0): # 为什么这里arg要初始化为0.0 我试了不给arg赋值也能得到相同结果
        return float.__new__(cls, arg*1.8 + 32)

print(C2F(32)) # 这里传进去的 明明不是一个浮点数啊，是int？ 为什么程序不会报错。




