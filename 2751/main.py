from sys import stdin
input = stdin.readline
for i in sorted(map(int, (input() for _ in range(int(input()))))): print(i)
