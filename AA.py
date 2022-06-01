
import sys
#sys.stdin=open("input.txt", 'rt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lt = 0
rt = N-1
while lt <= rt:
    mid = (lt + rt) // 2
    if lst[mid] == M:
        print(mid+1)
        break
    elif lst[mid] > M:
        rt = mid - 1
    else:
        lt = mid + 1