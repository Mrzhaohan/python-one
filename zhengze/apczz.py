import re

def who(x):
    news = []
    filex = open(x, 'r')
    whlie True:
        read = filex.readline()
        r = r'^(?P<ip_add>[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*\".*\"\s[0-9]{3}\s(?P<how_big>[0-9]*).*'
        sech = re.match(read, r, re.M|re.I)
        alluser = sech.groupdict()
        news.append(alluser)
        if read == '':
            break
    filex.close()
    back = {}
    for i in news:
        if i[ip_add] in back.keys():
            back[i[ip_add]]=i[how_big]
            back[i[ip_add]]=back[i[ip_addr]]+int(i[how_big])
        else:
            back[i[ip_add]]=int(i[how_big])
    return  back

if __name__ =='__main__':
    myfile = who('./access_log')
    for i in myfile.keys():
        print(i+myfile[i])
            

