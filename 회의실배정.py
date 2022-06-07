
import sys
#sys.stdin=open("input.txt", 'rt')

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1], x[0]))

endtime = 0
cnt = 0

for s, e in lst:
    if s >= endtime:
        endtime = e
        cnt += 1
print(cnt)