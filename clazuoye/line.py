class point():
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def set_x(self,x):
        self.x=x
    def get_x(self):
        return self.x
    def set_y(self,y):
        self.y=y
    def get_y(self):
        return self.y
    def whereis(self):
        print('({},{})'.format(self.x,slef.y))

class line():
    def __init__(self, x=0, y=0, w=1, z=1):
        self.x=x
        self.y=y
        self.w=w
        self.z=z
        self.begin=(self.x,self.y)
        self.end=(self.w,self.z)
    def set_begin(self, x, y):
        self.x=x
        self.y=y
        self.begin=(self.x,self.y)
    def set_end(self, w, z):
        self.w=w
        self.z=z
        self.end=(self.w,self.z)
    def how_long(self):
        a=self.w-self.x
        b=self.z-self.y
        longx=a*a+b*b
        longx=float(longx)
        lg=longx**0.5
        return lg
