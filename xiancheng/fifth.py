from threading import Thread,Condition
import time

class Producer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self,name=threadname)

    def run(self):
        global x
        con.acquire()
        if x == 10000000:
            con.wait()
            pass
        else:
            for i in range(10000000):
                x += 1
            con.notify()
        print(x)
        con.release()

class Consumer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name=threadname)

    def run(self):
        global x
        con.acquire()
        if x == 0:
            con.wait()
            pass
        else:
            for i in range(10000000):
                x -= 1
        print(x)
        con.release()
con = Condition()
x=0

p = Producer('Producer')
c = Consumer('Consumer')

p.start()
c.start()
p.join()
c.join()

print(x)
