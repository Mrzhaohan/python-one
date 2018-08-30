import os
def ql(x):
    a=os.listdir(x)
    for i in a:
        b=os.path.join(x,i)
        if 'tmp' in b:
            os.remove(b)

if __name__=='__main__':
    ql('/root/python/test')
