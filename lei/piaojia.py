class menpiao():
    price=100
    time=''
    people=''
    def ti(self):
        if self.time=='jie':
            self.price=self.price*1.2
    def pe(self):
        if self.people=='student':
            self.price=self.price/2


if __name__=='__main__':
    tw=menpiao()
    a=2*tw.price
    tw.time='jie'
    tw.ti()
    b=2*tw.price
    st=menpiao()
    st.people='student'
    st.pe()
    c=st.price
    st.time='jie'
    st.ti()
    d=st.price
    print(int((b-a)+(d-c)))
