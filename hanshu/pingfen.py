def pingfen(x):
    a=''
    x=int(x)
    if x <= 100 and x >= 90:
        a='A'
        return a
    elif x <= 89 and x >= 80:
        a='B'
        return a
    elif x <= 79 and x >= 70:
        a='C'
        return a
    elif x <= 79 and x >= 70:
        a='D'
        return a
    elif x <= 59 and x >= 0:
        a='E'
        return a
 
if __name__ == '__main__':
    a=input(":")
    b=pingfen(a)
    print(b)
