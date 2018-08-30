import urllib.request
import re
from threading import Thread,Condition
x = []
class MyThread(Thread):
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n
    def paqu(self):
        global x
        url = 'https://www.qiushibaike.com/pic/page/{}/'.format(self.n)
        user_agent = "Chrome/4.0 (compatible; MSIE 5.5;Windows NT)"
        page = urllib.request.Request(url, headers={"User-Agent": user_agent})
        html = urllib.request.urlopen(page)
        first = html.read().decode("utf-8")
        # r = r'(?<=\<div\sclass\=\"content\"\n\>\<span\>).*(?=\<\/span\>)'
        r = r'target="_blank">\n<img\s*?src=(.*?)alt=.*?\s*?/>'
        a = re.findall(r, first)
        # print(a)
        for i in a:
            a = i.strip().replace('\"', '')
            x.append(a)
        for i in x:
            num+=1
            r2 = r'.*?/([A-Z0-9a-z]*)\.jpg'
            name = re.findall(r2,i)
            print(name)
            down = "http:{}".format(i)
            urllib.request.urlretrieve(down, "./tt/{}.jpg".format(name[0]))
t1 = []
for n in range(2,10):
    t = MyThread(n)
    t1.append(t)

for i in t1:
    i.start()
