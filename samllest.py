#prathu and juu
a,b=map(str,input().split())
b=int(b)
l=len(a)-b
x=1
for i in range(0,l-1):
    x=x*10
#print(x)
if(b==0):
    print(a)
else:    
 while(1):
    x=str(x)
    n=a.count(x)
    #print(n)
    if(n>=1):
        print(x)
        break;
    else:
        x=int(x)
        x+=1
