'''编写一个计时器,将计时结果显示出来'''
#import time
#t=time.time()
#a='n'
#while a!='y':
#    a=input('是否暂停y')
#st=time.time()
#fd=st-t
#print('{:<4.2f}秒'.format(fd))
'''随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出'''
import time
z=[]
x=time.time()
b=str(x)
c=b[-2:]
d=int(c)
flag=True
while flag:
    flag=False
    if d==0:
        flag=False
    elif d%2==0:
        z.append('0')
        d=d/2
        flag=True
    elif d%2!=0:
        z.append('1')
        d=(d-1)/2
        flag=True
z.reverse()
n=''.join(z)
print('0x{}'.format(n))
'''删除元祖中的所有重复的元素，并生成一个列表'''
a=3,5,6,7,5,'df'
#b=list(a)
#print(b)
#c=list(set(b))
#a=tuple(c)
#print(a)
'''任意输入一个正整数,判断其是否为质数'''
#n=int(input('请输入数字：'))
#if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
#    print('{}是质数'.format(n))
#else:
#    print('{}不是质数'.format(n))
'''求得1到100之间有多少个质数'''
#k=0
#n=''
#z=''
#f=''
#for i in range(1,101):
#    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#         k+=1
#         n=n+'{}'.format(i)+' '
#         z='一百一内质数有：'+n+','
#         f=z+'总共{}个！'.format(k)
#print(f)
'''读入行数,输出以下形状
    假定输入的行数是4
(1)
    *
    * * 
    * * *
    * * * *
(2)
           *
        * * *
     * * * * *
  * * * * * * *'''
#n=int(input('请输入层数：'))
#print('(1)')
#for i in range(n):
#    x='* '
#    x=x*(i+1)
#    print(x)
#print('(2)')
#for k in range(n):
#    x='* '
#    if n%2==0:
#        o=int(n-k)
#        c=' '*o
#        x=c+x*(k+1)
#        print(x)
#    elif n%2!=0:
#        o=int(n-k)
#        c=' '*o
#        x=c+x*(k+1)
#        print(x)
'''求得斐波那契数列前二十项，存到列表中，并求得倒叙'''
#nums =[]
#k = 1
#n = 1
#b = 0
#while k < 21:
#    nums.append(n)
#    c = n + b
#    b = n
#    n = c
#    k = k+1
#nums.reverse()
#print(nums)
