
import sys
#sys.stdin=open("input.txt", 'rt')

N, M = map(int, input().split())
p = list(map(int,input().split()))
p.sort()
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    cnt += 1
    if p[0] + p[-1] <= M:
        p.pop(0)
        p.pop()
    else:
        p.pop()
print(cnt)

