N = int(input())
l = list(range(1, N+1))
while len(l) - 1:
    l = l[1:]
    l.append(l.pop(0))
print(l)