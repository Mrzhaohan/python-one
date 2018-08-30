n=input('请输入：')
z={}
for i in n:
    if i in z:
        z[i]+= 1
    else:
        z[i]=1
for k,v in z.items():
    print('\'{}\'有{}个。'.format(k,v))
