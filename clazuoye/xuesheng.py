class student():
    def __init__(self, name, age, score)
        self.name = name
        self.age = age
        self.score = score
        self.dic={self.name:self.age,self.score}
    def get_age(self,x)
        return self.dic[x][0]
    def max_score(self):
        score_C={}
        score_M={}
        score_E={}
        for i in self.dic.keys():
            a=self.dic[i][1]
            for n in a.keys():
                if n=='语文':
                    score_C[n]= a[n]
                elif n =='数学':
                    score_M[n]= a[n]
                elif n =='英语':
                    score_E[n]= a[n]
        flag = True
        for v in score_C.keys():
            if flag:
                max_score = score_C[i]
                max_name = i
                flag =False
                continue
            else:
                if score_C[i]>max_score:
                    max_score = score_C[i]
                    max_name = i
            self.c=[max_name:max_score] 
        flag = True
        for v in score_M.keys():
            if flag:
                max_score = score_M[i]
                max_name = i
                flag =False
                continue
            else:
                if score_M[i]>max_score:
                    max_score = score_M[i]
                    max_name = i
            self.m=[max_name,max_score] 
        flag = True
        for v in score_E.keys():
            if flag:
                max_score = score_E[i]
                max_name = i
                flag =False
                continue
            else:
                if score_E[i]>max_score:
                    max_score = score_C[i]
                    max_name = i
            self.e=[max_name,max_score] 
        print('''
语文最高分获得者是{},分数是{};
数学最高分获得者是{},分数是{};
英语最高分获得者是{},分数是{};
'''.format(self.c[0],self.c[1],self.m[0],self.m[1],self.e[0],self.e[1]))


