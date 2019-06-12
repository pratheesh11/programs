#prathu
importsys
def cfreq(s) :
    dic11 = {}
    for c1 in s1 :
        dic11[c1] = dic11.get(c1,0) + 1
    return dic11

s1 = input()
n1 = len(s1)
dic11 = cfreq(s1)
Lk1 = list(dic11.keys())

for j1 in range(n1-2,-1,-1) :
      for c1 in Lk1 :
        k1 = 0
        for i1 in range(0,n1-j1) :
            li1, ri1 = i1,j1+i1
            s21 = s1[li1:ri1 + 1]
            #print(c,s2)
            if c1 in s21 :
                k1 += 1
        if k1 == n1-j1 :
            #print('c,k',c,k)
            c21 = c1
            k21 = k1
            len21 = j1+1
print(len21)
