import time
def deco(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        msecs=(end_time-start_time)*1000
        print('->elapsedtime{}ms'.format(msecs))
    return wrapper

def myfunc():
    print('start myfunc')
    time.sleep(0.6)
    print('end myfunc') 

print('myfunc is:',myfunc.__name__)
myfunc = deco(myfunc)
print('myfunc is:',myfunc.__name__)
myfunc()
