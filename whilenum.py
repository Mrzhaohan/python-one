import random as rd
i = 0
isgoon='y'
n=0
while isgoon=='y':
    x= rd.randint(1,100)
    while i!=x or i=='q':
        i=input('猜一个100以内的数字：')
        if i.isdigit()==False:
            print('请输入整数！')
        else:
            i = int(i)
            if i < x:
                print('比它小哦')
            elif i > x:
                print('比它大哦')
        n+=1
        if i == x:
            print('猜对了！就是{},一共猜了{}次'.format(x,n))
    isgoon=input('是否继续游戏？(y继续,q退出)')
    n=0
print('真可惜再见！')
