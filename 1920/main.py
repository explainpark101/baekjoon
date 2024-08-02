from sys import stdin

input = stdin.readline
input()
nums = set(map(int, input().split(" ")))
input()
checks = map(int, input().split(" "))
for _ in checks:
    print(int(_ in nums))