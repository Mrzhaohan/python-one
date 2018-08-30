class A():
    name='A class'
    __txt='i am father'
    def say(self):
        print('i am in {}, {}'.format(self.name,self.__txt))

class B():
    name='B class'
    def run(self):
        print('i can run')

class C(A,B):
    __txt='i am son'
    def say(self):
        print('i am in {}, {}'.format(self.name,self.__txt))

a=A()
a.say()
b=B()
b.run()
c=C()
c.say()
c.run()
