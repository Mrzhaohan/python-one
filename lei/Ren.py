class Ren():
    def __init__(self,name,age,money):
        print('start init......')
        self.name = name
        self.age = age
        self.__money = money
    def __say(self):
        print('hello i am {} i have {} yuan'.format(self.name,self.__money))
    def lie(self,some='friend'):
        if some == 'xinxin':
            self.__say()
        else:
            print('i have 0 yuan')


if __name__ == '__main__':
    zhaohan=Ren('zhaohan',21,100000)
    zhaohan.lie('xinxin')
