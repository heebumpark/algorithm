
import sys
#sys.stdin=open("input.txt", 'rt')
MAX = 0
K, N = map(int, input().split())
lst = []

def Count(num): #총 몇개의 랜선 조각이 나오는지 반환
    cnt = 0
    for i in lst:
        cnt += (i // num)
    return cnt

for i in range(K):
    lst.append(int(input()))
    if lst[i] > MAX:
        MAX = lst[i]

lt = 1
rt = MAX

while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) < N:
        rt = mid-1
    else:
        res = mid
        lt = mid+1

print(res)