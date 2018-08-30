def jiecheng(n):
    if n==0 or n==1:
        return 1
    else:
        a=n*jiecheng(n-1)
        return a
def jieba(n):
    a=1
    b=0
    for i in range(1,n+1):
        a*=i
    return(a)    
if __name__=='__main__':
    print(jiecheng(5))
    print(jieba(5))
