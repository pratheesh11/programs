#prathu
#pratheesh
a,b=map(str,input().split())
u=0
f=0
for i in range(0,len(a)):
   if(len(b)<=i):
       f=1
       break;
   else:
     if(a[i]==b[i]):
        u+=1
if(f==1):
    print(len(a)-u)
else:    
    print(len(b)-u)
