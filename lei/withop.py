class MyFile():
    ''' '''
    def __init__(self, fn, mod):
        self.fn = fn
        self.mod = mod

    def __enter__(self):
        '''with开始时执行'''
        print('start')
        try:
            self.fobj = open(self.fn, self.mod)
        except FileNotFoundError:
            pass
        return self.fobj

#    def myRead(self):
#        '''读取文件内容'''
#        try:
#            return self.fobj.read() 
#        except FileNotFoundError:
#            pass
#
    def __exit__(self, e, m, d):
        '''with结束时执行'''
        print('end')

if __name__=='__main__':
    with MyFile('./fuzi.py','r') as mt:
        print('with end')
        print(mt.readline())
