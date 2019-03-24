#pratheesh
#include<stdio.h>
int main()
{
int n,m,diff,sum=0,temp,i;
scanf("%d%d%d",&n,&m,&diff);
for(i=0;i<n;i++)
{
temp=sum+m;
sum=temp;
m=m+diff;
}
printf("%d",temp);
return 0;
}
