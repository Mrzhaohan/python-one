#def jduiz(x):
#    if x>=0:
#        return x
#    else:
#        return -x
#
#n=int(input(':'))
#b=jduiz(n)
#print(b)

def fb_baibei(x):
    return x*100

#a=fb_baibei(5)
#print(a)
def mylen(x):
    n=0
    for i in x:
        n+=1
    return n
#
#z=input(':')
#b=mylen(z)
#print(b)

def f(y,x='5'):
    print('你好 您的{}元{}冰淇淋 请拿好'.format(x,y))
if __name__=='__main__':
    t=('香草','5')
    z={'x':6,'y':'巧克力'}
    f(*t)
    f(**z)
