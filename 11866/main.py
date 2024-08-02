N, K = map(int, input().split())
index = 0
r = list()
_r = set()
mod = lambda a,b:a%b
for _ in range(N):
    for i in range(K):
        index = mod(index+1, N)
        while index in _r:
            index = mod(index+1, N)
    r.append(index)
    _r.add(index)
r = (_ if _ else N for _ in r)
print(f"<{', '.join(map(str, r))}>")