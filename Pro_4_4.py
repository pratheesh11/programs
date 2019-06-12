#prathu
X1,Y1=map(int,input().split())
D1=0
Li=[]
for i in range(X1):
      Li.append(input())
for i in range(X1):
      for j in range(Y1-1):
            if(Li[i][j]!='R' and Li[i][j+1]!='R'):
                  D1+=3
            elif(Li[i][j]!='G' and Li[i][j+1]!='G'):
                  D1+=5
print(D1)
