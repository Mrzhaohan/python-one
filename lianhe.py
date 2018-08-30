n=0
z=''
x='1'
nums=input('请输入所想的整数和：')
if nums.isdigit():
    nums=int(nums)
    for k in range(1,nums+1):
        n+=k
        if k==1:
            x='1'
            z=x+"={}".format(n)
        else:
            x=x+'+{}'.format(k)
            z=x+'={}'.format(n)
        print(z)
else:
    print('输入的不是整数！')
