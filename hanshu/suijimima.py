import random
import string
def sm(n=6):
    '''随机生成N位密码，默认为6位'''
    mm=''
    hc=string.ascii_letters
    a=0
    b=0
    for i in range(n):
        a=random.randint(1,3)
        if a == 1:
            b=random.randint(0,26)
            mm+=hc[b]
        if a == 2:
            b=random.randint(26,52)
            mm+=hc[b]
        if a == 3:
            b=random.randint(0,10)
            mm+=str(b)
    return mm

if __name__ == '__main__':
    a=sm()
    print(a)
