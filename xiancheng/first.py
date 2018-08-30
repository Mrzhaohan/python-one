import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10):
            print('this is {}{}'.format(self.name,i))
            time.sleep(0.5)


t1 = MyThread('xinxin')
t2 = MyThread('zhaohan')


t1.start()
t1.join()
t2.start()

print('main end')
