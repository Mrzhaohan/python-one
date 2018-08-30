class list_new():
    def __init__(self,*agrs):
        self.__mylist=[i for i in agrs]
    
    def __add__(self,x):
        return [i+x for i in self.__mylist]
    
    def __sub__(self,x):
        return [i-x for i in self.__mylist]
 
    def __mul__(self,x):
        return [i*x for i in self.__mylist]

    def __div__(self,x):
        return [i/x for i in self.__mylist]

    def show(self):
        print(self.__mylist)

l=list_new(1,2,3,4,5,6)

l.show()

print(l+7)
