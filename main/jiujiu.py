c=0
x=''
for i in range(1,10):
    z=''
    for k in range(1,i+1):
        for n in range(i,10):
            c=i*k
            x=('{}*{}={}'.format(k,i,c))
        z=z+' '+x
    print(z)
