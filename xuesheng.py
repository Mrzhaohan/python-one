''''''
'''
2.完成学生管理系统1.0版
    学生类：
        成员：
            名字
            学号
            成绩
        方法：
            更改成绩
            更改名称
    增删改查——》存列表/存文件
'''
class Student():
    nums = 0
    def __init__(self,name,num,secore):
        self.name = name
        self.__num = num
        self.secore = secore
        Student.nums += 1
    def getnum(self):
        return self.__num
if __name__ == '__main__':
    lan = {}
    print('                      ######################')
    print('                      欢迎来到学生管理系统：')
    print('                      ######################')
    iscontinue = 'y'
    a = 0
    while a != '5' or a != '':
        a = input('''                    ###########################
                        录入学生信息请输入1
                        修改信息请输入2
                        查找信息请输入3
                        删除信息请输入4
                        退出系统请输入5
                   请输入：''')
        if a == '1':
            while iscontinue == 'y' or iscontinue == 'Y':
                me = input('请输入学生姓名：')
                nu = str(input('请输入该学生学号：'))
                se = input('请输入该学生分数：')
                p = Student(me,nu,se)
                lan[p.getnum()]=(p.name,p.secore)
                iscontinue = input('是否继续（y/n）')
        elif a == '2':
            while iscontinue == 'y' or iscontinue == 'Y':
                nu = input('这个学生的学号是：')
                me = input('请输入学生姓名：')
                se = input('请输入该学生分数：')
                lan[nu]=(me,se)
                iscontinue = input('是否继续（y/n）')
        elif a == '3':
            while iscontinue == 'y' or iscontinue == 'Y':
                nu = input('这个学生的学号是：')
                if nu == '':
                    print(lan)
                else:
                    print('姓名：{},成绩：{}'.format(lan[nu][0],lan[nu][1]))
                    iscontinue = input('是否继续（y/n）')
        elif a == '4':
            while iscontinue == 'y' or iscontinue == 'Y':
                nu = input('这个学生的学号是：')
                del lan[nu]
                iscontinue = input('是否继续（y/n）')
        elif a == '5' or a == '':
            break
        iscontinue = 'y'
    print('感谢使用')
