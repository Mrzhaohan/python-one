#开始界面
print('你他马有号吗？')
iskey=input('1you2meiyou:')
if iskey =='2':
    passwd=open('password.py','a+')
    user=input('shunimadezhanghao:')
    pasd=input('shunimademima:')
    ispasd=input('zaishuyibianmima:')
    if pasd==ispasd:
        passwd.write('{}:{}'.format(user,pasd))
        print('zhucechenggong,{}n\
idemimashi{}'.format(user,pasd))
    else:
        for i in '123':
            print('mimavutongyi!')
            user=input('shunimadezhanghao:')
            pasd=input('shunimademima:')
            ispasd=input('zaishuyibianmima:')
            if pasd==ispasd:
                passwd.write('{}:{}'.format(user,pasd))
                print('zhucechenggong,{}n\
idemimashi{}'.format(user,pasd))
                break
    passwd.colse
elif iskey=='1':
    passwd=open('password.py','a+')
    
