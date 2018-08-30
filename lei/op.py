class file_open():
    def __init__(self,z):
        '获取路径'
        self.fileway=z
    def changenumber(self):
        '读取文件并加行号（字典）显示'
        n=0
        dic={}
        b=open(self.fileway,'a+')
        while True:
            a=b.readline()
            n+=1
            dic[n]=a
            if a='':
                break
        print(a)
        return a
        b.closei()
    
    def manychange(self,x,y):
        '提供内容追加的方法'
        b=open(self.fileway,'a+')
        s=b.read()
        b.close()
        a=s.split('\n')
        a.insert(x-1,y)
        s='\n'.join(a)
        b=open(self.fileway,'w')
        b.write(s)
        b.close()

    def inpn(self,*x):
        '一次写入多行（列表）'
        a=[]
        b=open(self.fileway,'a+')
        while True:
            c=b.readline()
            a.append(c)
            if a='':
                b.close()
                break
        b=[i for i in x]
        a=a+b
        print(a)
