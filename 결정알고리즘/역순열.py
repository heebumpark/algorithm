import sys
#sys.stdin=open("input.txt", 'rt')

N = int(input())
rev = list(map(int, input().split()))
original = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if original[j] == 0:
            if cnt == rev[i]:
                original[j] = i+1
                break
            cnt += 1

for num in original:
    print(num, end=" ")       
    






