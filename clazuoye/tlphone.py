import os
class tlphone():
    def __init__(self):
        self.dic={}
        t=open('/root/python/test/tlphone.txt','r')
        while True:
            line=t.readline()
            line = line.strip()
            linep = line.split(' ')
            self.dic[linep[0]]=linep[1]
            if line=='':
                break
            line.close()
    def add_man(self, name, number):
        '添加联系人'
        self.dic[name]=number
        t=open('/root/python/test/tlphone.txt','w')
        for i in self.dic.keys():
            t.write(i+' '+self.dic[i]+ '\n')
        t.close()
        print('以添加联系人')
    def del_man(self, name):
        '删除联系人'
        if name in self.dic.keys():
            self.pop(name)
            for i in self.dic.keys():
                t.write(i+' '+self.dic[i]+ '\n')
            t.close()
        else:
            raise NameError('have no man in tlphone!')
    def find_man(self,name):
        '查找联系人'
        if name in self.dic.keys():
            print('{}的联系电话是{}'.format(name,self.dic[name]))
        else:
            raise NameError('have no man in tlphone!')
    def change_man(self, name, number):
        '修改联系人'
        if name in self.dic.keys():
            self.dic[name]= number
            print('联系人{}以修改电话为{}'.format(name,number))
        else:
            raise NameError('have no man in tlphone!')

