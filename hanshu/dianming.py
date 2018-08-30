import random
def dianming():
    a=''
    b=0
    z=['a','b','v','c','d','e']
    b=random.randint(0,len(z)-1)
    a=z[b]
    return a

if __name__ == '__main__':
    a=dianming()
    print(a)
