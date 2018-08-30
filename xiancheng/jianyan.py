import threading
import subprocess
import queue
import time
def pig(num):
    n = num.get()
    num.task_done()
    ip = '172.25.2.{}'.format(n)
    ret = subprocess.call('ping -c 1 {}'.format(ip),shell=True, stdout=open('say', 'w'), stderr=subprocess.STDOUT)
    if ret==0:
        print('172.25.2.{}'.format(n))
    else:
        print('hao')

num = queue.Queue()
for i in range(0,256):
    num.put(i)
#for i in range(255):
#    th = threading.Thread(target=pig, args=(num,))
#    th.setDaemon(True)
#    th.start()
while not num.empty():
    t1 = threading.Thread(target=pig, args=(num,))
    t1.start()
    t2 = threading.Thread(target=pig, args=(num,))
    t2.start()
