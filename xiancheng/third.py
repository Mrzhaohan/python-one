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
print(t3.isAlive())

t2.daemon = True
t2.start()
print('t2 name:',t2.getName())
print('t2 name:',t2.setName('TTTT2222'))
print('t2 name:',t2.getName())
t3.start()
print(t3.isAlive())
t3.join()
#t1.join()

print('main stop')
