import random as rd
def move(i, x, y):
    for v in range(1,i+1):
        b = rd.randint(1,4)
        if b == 1:
            if x+1 <= 10:
               x = x + 1
            else:
                v -= 1
        elif b == 2:
            if x-1 >= 0:
                x = x - 1
            else:
                v -= 1
        elif b == 3:
            if y+1 <= 10:
                y = y + 1
            else:
                v -= 1
        #elif b == 4:
        #    if y-1 >= 0:
        #        y = y - 1
        #    else:
        #        v -= 1
        #elif b == 5:
        #    if x+1 <= 10 and y+1 <= 10:
        #        x = x + 1
        #        y = y + 1
        #    else:
        #        v -= 1
        #elif b == 6:
        #    if x+1 <= 10 and y-1 >= 0:
        #        x = x + 1
        #        y = y - 1
        #    else:
        #        v -= 1
        #elif b == 7:
        #    if x-1 >= 0 and y-1 >= 0:
        #        x = x - 1
        #        y = y - 1
        #    else:
        #        v -= 1
        #elif b == 8:
        #    if x-1 >= 0 and y+1 <= 10:
        #        x = x - 1
        #        y = y + 1
        #    else:
        #        v -= 1
        return [x,y]
class animal():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.a=[self.x,self.y]
    def run(self):
        a = rd.randint(1,2)
       # for i in range(a):
        if self.x=='die' or self.y=='die':
            pass
        else:
            b=move(a,self.x,self.y)
            self.tili -= 1
            self.a = b
    def where_is(self):
        return self.a
    def life(self):
        if self.tili <= 0:
            self.x='die'
            self.y='die'
            self.a=[self.x,self.y]
    @property
    def say(self):
        return '哈哈哈哈!'
class turhan(animal):
    
    def __init__(self,x=5,y=5):
        self.x = x
        self.y = y
        self.tili=100
        self.a=[self.x,self.y]
    def run(self):
        a = rd.randint(1,2)
       # for i in range(a):
        if self.x=='go die' or self.y=='go die':
            pass
        else:
            b=move(a,self.x,self.y)
            self.tili -= 1
            self.a = b
    def whereT(self):
        return self.a
    def life(self):
        if self.tili <= 0:
            print('骚晗屎了')
            self.x='go die'
            self.y='go die'
            self.a=[self.x,self.y]
        else:
            return self.tili
    def eat(self):
        self.tili+=10
    @property
    def say(self):
        return '哈哈哈哈!敢惹我龟丞相'

class fish(animal):
    def __init__(self,x=rd.randint(1,10),y=rd.randint(1,10)):
        self.x=x
        self.y=y
        self.a=[self.x,self.y]
    def run(self):
         
        if self.x=='' or self.y=='':
            pass
        else:
            b=move(1,self.x,self.y)
            self.a=b
    def whereF(self):
        return self.a
    def die(self):
        self.x='' 
        self.y=''
        self.a=[self.x,self.y]
    @property
    def laugh(self):
        return '小样!还想吃我'

def my_map():
    return ['#','#','#','#','#','#','#',"#",'#','#']
def where(y):
    a=my_map()
    b=my_map()
    c=my_map()
    d=my_map()
    e=my_map()
    f=my_map()
    g=my_map()
    h=my_map()
    z=my_map()
    j=my_map()
   
    for i in y.keys():
        x=y[i]
        try:
            if i == 1:
                a[x-1]='*'
            elif i== 2:
                b[x-1]='*'
            elif i== 3:
                c[x-1]='*'
            elif i== 4:
                d[x-1]='*'
            elif i== 5:
                e[x-1]='*'
            elif i== 6:
                f[x-1]='*'
            elif i== 7:
                g[x-1]='*'
            elif i== 8:
                h[x-1]='*'
            elif i== 9:
                z[x-1]='*'
            elif i== 10:
                j[x-1]='*'
        except :
            pass
    q=(' '.join(a)+'\n'+' '.join(b)+'\n'+' '.join(c)+'\n'+' '.join(d)+'\n'+' '.join(e)+'\n'+' '.join(f)+'\n'+' '.join(g)+'\n'+' '.join(h)+'\n'+' '.join(z)+'\n'+' '.join(j)+'\n')
    return q
if __name__ == '__main__':
    b = {1:3,5:6,7:8,4:6}
    c= where(b)

