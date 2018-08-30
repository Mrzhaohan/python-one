def diejia(x,y):
    z=0
    b=''
    c=''
    a=''
    x=str(x)
    for i in range(1,y+1):
        a=x*i
        if i == 1:
            b=a
        else:
            b=b+'+'+a
        z+=int(a)
    c=b+'='+str(z)
    return c

if __name__ == '__main__':
    x=int(input(':'))
    y=int(input(':'))
    o=diejia(x,y)
    print(o)
