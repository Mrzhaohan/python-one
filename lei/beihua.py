class flower():
    flow=''
    color=''
    name=''
    def fenlei(self):
        if self.name=='迎春':
            self.color='红色'
            self.flow='大瓣'
        elif self.name=='樱花':
            self.color='粉色'
            self.flow='小瓣'


a=flower()
b=flower()
a.name='迎春'
b.name='樱花'
a.fenlei()
b.fenlei()
print('{}是{}的{}花'.format(a.name,a.color,a.flow))
print('{}是{}的{}花'.format(b.name,b.color,b.flow))
