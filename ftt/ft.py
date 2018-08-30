#!/usr/bin/env python
from ftplib import FTP

class MyFtp():
    def __init__(self, x, y='', z=''):
        self.ftp = FTP(x)
        if y=='' or z=='':
            self.ftp.login()
        else:
            self.ftp.login(y,z)
    def download(self, filename, filepath):
        comm = "RETR" + filename
        self.ftp.retrbinary(comm, open(filepath, 'wb').write())
        print('下载成功')
    def puton(self, filepath, filename):
        comm = "STOR" + filepath
        self.ftp.storbinary(comm, open(filename, 'rb'))
        print('上传成功')
    def lis(self):
        self.ftp.retrlines('LIST')
    def cd(self, x):
        self.ftp.cwd(x)
    def close(self):
        self.ftp.close()


if __name__=='__main__':
    fname = input('请输入ftp地址：')
    username = input('请输入用户名(默认匿名用户):')
    if username == '':
        ftp = MyFtp(fname)
    else:
        userpass = input('请输入用户密码:')
        ftp = MyFtp(fname, username, userpass)
    path = ''
    while True:
        point = input('{}>'.format(path))
        if point=='ls':
            ftp.lis()
        elif point=='cd':
            path = input('请输入地址:')
            try:
                ftp.cd(path)
            except:
                raise NameError('该目录不存在')
        elif point=='dl':
            filename = input('请输入要下载的文件:')
            filepath = input('请输入下载路径：')
            try:
                ftp.download(filename, filepath)
            except:
                raise NameError('文件名或路径不合法')
        elif point=='pt':
            filepath = input('请输入上传文件的路径:')
            filename = input('请输入上传文件民:')
            try:
                ftp.puton(fielpath, filename)
            except:
                raise NameError('文件名或路径不合法')
        elif point=='exit':
            ftp.close()
            print('bye bye~')
            break   
