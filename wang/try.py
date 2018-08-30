import urllib.request

qsbk_url = 'http://www.qiushibaike.com/'
user_agent = 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(qsbk_url,headers={'User_Agent':user_agent})
page = urllib.request.urlopen(req)
html = page.read().decode('utf-8')
print(html)
