import truhan

zhaohan = truhan.turhan()
fish1 = truhan.fish()
fish2 = truhan.fish()
fish3 = truhan.fish()
fish4 = truhan.fish()
fish5 = truhan.fish()
n = 5
while True:
    a=zhaohan.whereT()
    b=fish1.whereF()
    c=fish2.whereF()
    d=fish3.whereF()
    e=fish4.whereF()
    f=fish5.whereF()
    ma={a[0]:a[1],b[0]:b[1],c[0]:c[1],d[0]:d[1],e[0]:e[1],f[0]:f[1]}
    w=truhan.where(ma)
    r='''龟的位置是{},鱼群的位置是{}{}{}{}{}'''.format(a,b,c,d,e,f)+'\n'+'龟的体力是{}'.format(zhaohan.tili)+'\n'+w
    print('\r{}'.format(r))
    zhaohan.run()
    fish1.run()
    fish2.run()
    fish3.run()
    fish4.run()
    fish5.run()
    if a==b:
        zhaohan.eat()
        n-= 1
        fish1.die()
    elif a==c:
        zhaohan.eat()
        n-= 1
        fish2.die()
    elif a==d:
        zhaohan.eat()
        n-= 1
        fish3.die()
    elif a==e:
        zhaohan.eat()
        n-= 1
        fish4.die()
    elif a==f:
        zhaohan.eat()
        n-= 1
        fish5.die()
    k = zhaohan.life()
    if zhaohan.tili <  0 or zhaohan.tili==0:
        if b[0]!='':
            print('a说：',fish1.laugh)
        if c[0]!='':
            print('b说：',fish2.laugh)
        if d[0]!='':
            print('c说：',fish3.laugh)
        if e[0]!='':
            print('d说：',fish4.laugh)
        if f[0]!='':
            print('e说：',fish5.laugh)
        break
    elif zhaohan.tili > 0:
        pass
    if n == 0:
        print('赵晗说：',zhaohan.say)
        break
