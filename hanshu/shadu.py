import os
def blfp(path):
    file_name_list=os.listdir(path)
    g=[]
    for file_name in file_name_list:
        file_path_name=os.path.join(path,file_name)
        if os.path.isfile(file_path_name):
            g.append(file_path_name)
        else:
            blfp(file_path_name)
    return g

def sd(path):
    g=blfp(path)
    n=0
    for i in g:
        file_name=open(i,'r')
        while True:
            b=file_name.readline()
            if 'milomilomilo' in b:
                n+=1
                os.rename(i,'virus-{}.bak'.format(n))
                break
            elif b=='':
                break

if __name__ == '__main__':
    sd('/root/python/test')
