#pratheesh
nq= input().split()
n = int(nq[0])
q = int(nq[1])

in_nums = list(map(int, input().split()))

for _ in range(q):
    u, v = map(int, input().split())
    s = sum(in_nums[u-1:v])
    print(s)
