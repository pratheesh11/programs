#prathu
n1,k1 = map(int,input().split())
l1 = list(map(int,input().split()))
c1= 0
for i in l1:
    if(i+k1 <=5):
        c1+=1
print(c1//3)
