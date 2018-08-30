class List_info():
    def __init__(self,x):
        self.lis=x
    def appd(self,x):
        '添加元素'
        if isinstance(x,int):
            self.lis.append(x)
        elif isinstance(x,str):
            self.lis.append(x)
        else:
            raise TypeError('only int or str')
        return self.lis
    def output(self,x):
        try:
            a = self.lis[x]
            print(a)
        except :
            raise TypeError('only int can do this')
    def addal(self,li):
        for i in li:
            self.lis.append(i)
        return self.lis
    def delend(self):
        self.lis.pop(-1)
        return self.lis
