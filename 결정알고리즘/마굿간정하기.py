
import sys
#sys.stdin=open("input.txt", 'rt')

def checker(distance):
    cnt = 1
    index = 0
    for i in range(len(lst)):
        if lst[i] - lst[index] >= distance:
            cnt +=1 
            index = i
    return cnt


N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

lt, rt = lst[0], lst[-1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if checker(mid) >= C:
        res = mid
        lt = mid+1  
    else:
        rt = mid-1
print(res)
