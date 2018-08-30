class juxing():
    def __init__(self,l,w):
        self.__chang=l
        self.__kuan=w
    def setLongWeide(self,l,w):
        '赋予长度值'
        self.__chang=l
        self.__kuan=w
    def getLong(self):
        '获得长度值'
        return self.chang
#    def setWeide(self,w):
#        '赋予宽度值'
#        self.__kuan=w
    def getWeide(self):
        '获得宽度值'
        return self.kuan
    def zhouchang(self):
        '获得周长'
        zhouchang=2*(self.__chang+self.__kuan)
        print(zhouchang)
    def panduan(self):
        '判断是否是正方形'
        if self.__chang==self.__kuan:
            print('zhengfanxing')
        else:
            print('changfangxing')
    def mianji(self):
        '求面积'
        mian=self.__chang*self.__kuan
        print(mian)

class zhengfang(juxing):
    def __init__(self,l):
        self.__long=l

    def getLongWeide(self,l):
        self.__long=l
    
    def setLong(self,l):
        return self.__long

    def mianji(self):
        print(self._long*self.__long)

    def zhouchang(self):
        print(self.long*4)

if __name__=='__main__':
#    a=int(input('chang'))
#    b=int(input('kuan'))
#    c=juxing(1,2)
#    c.mianji()
#    c.setLong(a)
#    c.setWeide(b)
#    c.mianji()

