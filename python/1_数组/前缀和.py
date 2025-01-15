n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
p = []
sum = 0
for i in arr:
    sum+=i
    p.append(sum)
print(p)