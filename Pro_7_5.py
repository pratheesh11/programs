#prathu
y1,y2 = map(int,input().split())
m = list(map(int,input().split()))
amount = int(input())
total = (sum(m)-m[y2])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
