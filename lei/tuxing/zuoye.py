class sanjiaoxing():
    def __init__(self,a,b,c):
        '输入三角形三条边的值'
        self.__a=a
        self.__b=b
        self.__c=c

    def getA(self,a):
        self.__a=a

    def getB(self,b):
        self.__b=b

    def getC(self,c):
        self.__c=c

    def panduan(self):
        '判断三条边能否构成三角形，如不能报错'
        if self.__a+self.__b<=self.__c or self.__a+self.__c<=self.__b or self.__b+self.__c<=self.__a:
            raise Exception('a,b,c不能构成三角形')
            return False
        else:
            print('以生成三角形')
            return True

    def zhouchang(self):
        zhou=self.__a+self.__b+self.__c
        print('周长是{}'.format(zhou))

    def mj(self):
        p=(self.__a+self.__b+self.__c)/2
        s=p*(p-self.__a)*(p-self.__b)*(p-self.__c)
        s=float(s)**0.5
        print(s)

if __name__ == '__main__':
    c=sanjiaoxing(3,4,5)
    c.panduan()
    c.zhouchang()
    c.mj()
    c.getA(2)
    c.getB(1)
    c.getC(3)
    if c.panduan():
        c.zhouchang()
