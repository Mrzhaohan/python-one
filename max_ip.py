l = ["172.16.3.1", '172.16.1.5', '172.15.2.0', '172.16.3.1',\
 '172.16.3.1', '172.16.1.5']
z={}
for i in l:
    n=0
    for k in l:
        if i==k:
            n=n+1
    z[i]=n
flag=True
for i in z.keys():
    if flag:
        max_number=z[i]
        max_ip=i
        flag=False
        continue
    else:
        if  z[i]>max_number:
            max_number=z[i]
            max_ip=i
print('{}max,number is {}'.format(max_ip,max_number))
