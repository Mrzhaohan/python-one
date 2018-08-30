class Person():
    def __init__(self, f, l):
        '输入内容'
        self.l = l
        self.f = f
    @property
    def dull_name(self):
        '以变量形式获得内容'
        return '{}{}'.format(self.f,self.l)
    @dull_name.setter
    def dull_name(self,x):
        '修改或输入内容'
        a=x.split(' ')
        self.f=a[0]
        self.l=a[1]
class Free():
    def __init__(self):
        self.__fee = None
    def get__fee(self):
        return self.__fee
    def set__fee(self,value):
        self.__fee = value

f=Free()
print(f.get__fee())
zhaohan = Person('zhao','han')
print(zhaohan.dull_name)
zhaohan.dull_name='sao bi'
print(zhaohan.dull_name)
