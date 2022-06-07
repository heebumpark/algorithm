
import sys
#sys.stdin=open("input.txt", 'rt')

N = int(input())
mems = []
max_h = 0
max_w = 0
cnt = 0
for i in range(N):
    mems.append(list(map(int, input().split())))

mems.sort(reverse=True)
max_w = 0
for h, w in mems:
    if  w >= max_w:
        cnt += 1
        max_w = w
print(cnt) 