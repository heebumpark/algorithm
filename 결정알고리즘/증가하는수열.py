from collections import deque
import sys
#sys.stdin=open("input.txt", 'rt')

N = int(input())
nums = list(map(int, input().split()))
nums = deque(nums)
lst = []
res = ''
last = 0
cnt = 0
while nums:
    if last > max(nums[0], nums[-1]):
        break

    if nums[0] < nums[-1] and nums[0] > last:
        last = nums.popleft()
        res += 'L'
    elif nums[0] < nums[-1] and nums[0] < last:
        last = nums.pop()
        res += 'R'
    elif nums[0] > nums[-1] and nums[-1] > last:
        last = nums.pop()
        res += 'R'
    elif nums[0] > nums[-1] and nums[-1] < last:
        last = nums.popleft()
        res += 'L'
    
    cnt += 1

print(cnt)
print(res)


