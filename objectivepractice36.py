'''
this practice is from fishc forum (Practice 36), which is about the object-oriented programming
and how to establish a class and how to apply the funcs of the class.
'''

class Rectangle:
    # 为什么这里要属性确定一个初始值？小甲鱼设置了4，5；我设置None也可以啊。
    # 还有其他的初始化属性值的方法吗？
    # length = 5
    # width = 4
    length=None
    width = None


    def setRect(self):
        print('please enter the length and width to set a rectangle')
        self.length=float(input('length:'))
        self.width=float(input('width:'))

    def getRect(self):
        print('the length and width of this rectangle is: %.2f, %.2f, respectively' % (self.length, self.width))

    def getArea(self):
        print(self.length*self.width)


a = Rectangle()
a.setRect()
a.getRect()
a.getArea()

