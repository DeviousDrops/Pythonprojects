class Matrix:
    
    def __init__(self,r,c):
        self.r=r
        self.c=c
        self.m=[[0 for i in range(c)] for j in range(r)]
            
    def read(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                self.m[i][j]=int(input("Enter an element"))
                print(self.m)
        return self.m
    
    def add(self,m_):
        m3=[[0 for i in range(self.c)] for j in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                m3[i][j]=self.m[i][j]+m_[i][j]
        return m3

r=int(input("Enter no. of rows"))  
c=int(input("Enter no. of columns"))    
m1=Matrix(r,c)
m2=Matrix(r,c)
m1.read()
q=m2.read()
print(m1.add(q))
