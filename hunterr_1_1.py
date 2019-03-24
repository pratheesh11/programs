#pratheesh
n=int(input())
n1=list(map(int,input().split()))
b=[]
l=[0]*10
for i in range(0,len(n1)):
  l[n1[i]]+=1
a=max(l)
for i in range(0,len(l)):
  if a==l[i]:
    b.append(i)
if b==n1:
  print("unique")
else:
  for i in range(0,len(b)):
    if i==len(b)-1:
      print(b[i])
    else:
      print(b[i],end=' ')
