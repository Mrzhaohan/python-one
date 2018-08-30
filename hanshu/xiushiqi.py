import time

def deco(func):
    start_time=time.time()
    func()
    endtime=time.time()
    msecs=(end_time-start_time)*1000
    print('-> elapsed time:{} ms '.format(msecs))

def myfunc():
    print('start myfunc')
    time.sleep(0.6)
    print('end myfunc')

deco(myfunc)
myfunc()
