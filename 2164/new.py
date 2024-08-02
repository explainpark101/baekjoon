N = int(input())
l = list(range(1, N+1))
i = 0
while len(l) - 1:
    l = ([l[-1]] if len(l) & 1 else []) + l[1::2]
print(l[0])