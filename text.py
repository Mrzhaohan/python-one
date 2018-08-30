'''随机产生100以内的100个整形数，存储在一个列表中边历次列表，统计产生的数值有多少个偶数'''
import random as rd
c=[]
a=0
n=0
for i in range(100):
    a=rd.randint(1,101)
    c.append(a)
    if a%2==0:
        n+=1
print(c)
print('其中有{}个偶数'.format(n))
'''求得100内的所有的偶数序列中有多少个是5的倍数 '''
d=[]
f=0
for e in range(100):
    d.append(e)
    if e%2==0 and e%5==0:
        f+=1
print(d)
print('所有的偶数序列中有{}个是5的倍数'.format(f))
'''用户输入10个人的名字，随机选取一个人作为队长 '''
#g=[]
#for h in range(10):
#    j=input('请输入人名：')
#    g.append(j)
#l=rd.randint(1,11)
#k=g[l]
#print('队长是{}'.format(k))
'''不用python的sort方法，为列表排序'''
m=[1,7,5,6,4,9,8,3,2,5]
w=len(m)
flag = True
while flag:
    flag=False
    for s in range(w-1):
        t=m[s]
        u=m[s+1]
        if t>u:
            m[s],m[s+1]=m[s+1],m[s]
            flag=True
print(m)
