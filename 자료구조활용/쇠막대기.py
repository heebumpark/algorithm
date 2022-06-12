import sys
sys.stdin=open("input.txt", 'rt')

sticks = input()
lst = []
sum = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        lst.append(sticks[i])
    else:
        if sticks[i-1] == '(':
            lst.pop()
            sum += len(lst)
        else:
            lst.pop()
            sum += 1
            
print(sum)