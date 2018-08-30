a = input('请输入数字a：')
key=input('请输入运算符：')
b = input('请输入数字b：')
if a.isdigit()==False or  b.isdigit()==False:
    print('请输入整数字！！')
else:
    a=int(a)
    b=int(b)
    jsq={'+':a+b,
         '-':a-b,
         '*':a*b,
         '/':a/b}
    print(jsq.get(key,'对不起，目前只支持加减乘除'))
#    if key=='+':
#        c=a+b
#        print('{}{}{}={}'.format(a,key,b,c))
#    elif key=='-':
#        c=a-b
#        print('{}{}{}={}'.format(a,key,b,c))
#    elif key=='X' or key=='*':
#        c=a*b
#        print('{}{}{}={}'.format(a,key,b,c))
#    elif key=='%' or key=='/':
#        c=a/b
#        print('{}{}{}={}'.format(a,key,b,c))
#    else:
#        print('对不起，目前只支持加减乘除')
