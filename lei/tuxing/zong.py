import math
class tuxing():
    def say(self):
        print('这是一个图形')

class juxing(tuxing):
    def __init__(self,l,w):
        '设置长宽数据'
        self.__long=l
        self.__weide=w
    def mianji(self):
        '计算并返还面积'
        return self.__long*self.__weide
    def getLong(self):
        '获得长度'
        return self.__long
    def getWeide(self):
        '获得宽度'
        return self_weide
    def zhouchang(self):
        '计算并获得周长'
        return 2*(self.__long+self.__wedie)

class sanjiaoxing(tuxing):
    def __init__(self,a,b,c):
        '设置三边数据'
        self.__a=a
        self.__b=b
        self.__c=c
    def mianji(self):
        '计算面积并获得'
        q=(self.__a+self.__b+self.__c)/2
        s=q*((q-self.__a)*(q-self.__b)*(q-self.__c))
        s=s**0.5
        return s
    def zhouchang(self):
        '计算周长并获得'
        return self.__a+self.__b+self.__c
    def panduan(self):
        '判断能否构成三角形'
        if self.__a+self.__b>self.__c and self.__b+self.__c>self.__a and self.__a+self.__c>self.__b:
            print('{}{}{}可以构成三角形'.format(self.__a,self.__b,self.__c))
        else:
            raise TypeError('数据不合法，无法构成三角形')

class circle(tuxing):
    a=math.pi
    def __init__(self,b):
        '设置圆的半径'
        self.__b=b
    def zhouchang(self):
        '计算圆的周长并获得'
        return 2*self.a*self.__b
    def mianji(self)
        '计算圆的面积并获得'
        return (a*b*b)/2
    def getBanjing(self):
        return b
    
