class dayinji():
    color=''
    def dayin(self):
        if self.color=='黑白':
            print('黑白打印机打印黑白字')
        elif self.color=='彩色':
            print('彩色打印机能打印照片')
        else:
            print('只有彩色与黑色打印机！')



huipu1=dayinji()
huipu2=dayinji()
huipu1.color='黑白'
huipu2.color='彩色'
huipu1.dayin()
huipu2.dayin()

