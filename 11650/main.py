from sys import stdin
from functools import cmp_to_key
input = stdin.readline

coords = [tuple(map(int, _)) for _ in (input().split(" ") for i in range(int(input())))]
for x,y in sorted(coords, key=cmp_to_key(lambda a, b: a[0]-b[0] if a[0]-b[0] else a[1]-b[1])):
    print(f"{x} {y}")
