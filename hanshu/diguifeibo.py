def fb(n,list_num=[1,1]):
    i=0
    if n>2:
        while i<n:
            list_num.insert(i+2,list_num[i]+list_num[i+1])
            i+=1
        else:
            print(list_num)
        return list_num[n-1]
    else:
        return list_num[0]

if __name__ == '__main__':
    print(fb(5))
