class file_open():
    def __init__(self,z):
        '获取路径'
        self.fileway=z
    def open(self,x):
        try:
            self.op=open(z,x)
        except :
            print('请输入正确路径')
    def close(self,x):
        self.op.close()
       
