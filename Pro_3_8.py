#prathu
n=int(input())
m=list(map(int,input().split()))
m.sort()
s=0
c=0
for i in range(len(m)):
    if m[i]>=s:
        c=c+1
    s=s+m[i]
print(c)
