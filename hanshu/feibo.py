def feibo(n):
    a=0
    b=1
    for i in range(n):
        print(b)
        a,b=b,a+b

if __name__=='__main__':
    print(feibo(5))
