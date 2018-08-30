x=[]
for i in range(1,101):
    if i%3==0 or i%5==0:
        x.append(i)
c=sum(x)
print(x)
print(c)
