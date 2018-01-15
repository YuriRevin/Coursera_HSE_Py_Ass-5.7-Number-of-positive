a = 0
l = list(map(int, input().split()))
for i in range(0, len(l)):
    if l[i] > 0:
        a = a + 1
print(a)
