import threading
import time

def funcy(name):
    for i in range(5):
        print(name, i)
        time.sleep(0.5)

t1 = threading.Thread(target=funcy, args=('t1',))
t2 = threading.Thread(target=funcy, args=('t2',))
t3 = threading.Thread(target=funcy, args=('t3',))

t1.start()
t1.join()#优先权
t2.start()
t3.start()

#t1.join()

print('main stop')
