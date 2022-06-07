
import sys
#sys.stdin=open("input.txt", 'rt')

def divider(byte):
    cap = 0
    cnt = 1
    for i in lst:
        cap += i
        if cap > byte:
            cnt += 1
            cap = i
    return cnt

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lt = 1
rt = sum(lst)
res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if divider(mid) <= M:
        res = mid
        rt = mid-1
    else:
        lt = mid+1
        
print(res)
