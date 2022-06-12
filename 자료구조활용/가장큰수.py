import sys
#sys.stdin=open("input.txt", 'rt')

b_num, delete = map(int, input().split())
nums = []
for i in range(len(str(b_num))):
    nums.append(str(b_num)[i])
nums = list(map(int, nums))
new_nums = []

while len(nums) != 0:
    if len(new_nums) != 0 and new_nums[-1] < nums[0] and delete > 0:
        new_nums.pop()
        delete -= 1
       
        continue
    new_nums.append(nums.pop(0))
if delete != 0:
    new_nums = new_nums[:-delete]

for num in new_nums:
    print(num, end="")




