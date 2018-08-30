def qiepian(li):
    sr=li.split(':')
    return {'usr':sr[0],
            'group':sr[5],
            'miaoshu':sr[6]
           } 

def chuncun(x):
    for line in x:
        dict=qiepian(line)
        yield dict

def main():
    with open('/etc/passwd') as filepass:
        contines=filepass.readlines()
        lr=chuncun(contines)
    print(lr)
    for i in lr.keys():
        print(i,lr[i])


if __name__=='__main__':
    main()
