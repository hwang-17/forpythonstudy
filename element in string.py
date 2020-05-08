'''
编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。
题目来自小甲鱼课程 零基础python 课后练习
'''

def count(*strings):
    # 这里的length表示的是有几个参数
    length=len(strings)
    for eachstring in range(length):
        letter=0
        space=0
        digit=0
        others=0
        for element in strings[eachstring]:
            # 注意.isalpha计算字母的用法
            if element.isalpha():
                letter+=1
            # 注意.isdigit()的用法
            elif element.isdigit():
                digit+=1
            elif element==" ":
                space+=1
            else:
                others+=1
        print("第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。" %(eachstring+1, letter,digit,space,others))


count("I love fishc.com.", "I love you, you love me.")