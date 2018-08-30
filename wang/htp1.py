import urllib.request
page = urllib.request.urlopen('http://www.python.org')
print(page.read())
