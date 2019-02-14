n=int(input())
l=[]
temp=100000000
for i in range(0,n):
    x=input()
    l.append(x)
    temp1=len(x)
    if(temp1<temp):
        temp=temp1
        t=x
s=[]
#print(t)
for i in range(0,len(t)):
    s.append(0)
for i in range(0,len(t)):
    for j in range(0,n):
        m=l[j]
        #print(m)
        #print(s[i],ord(m[i]))
        if(t[i]==m[i]):
              s[i]=s[i]+1
j=0
#print(s)
for i in range(0,len(s)):
    if(s[i]==n):
        print(t[j],end="")
        j+=1
    else:
        break;
