import re, sys
input = sys.stdin.readline
nums = []
for _ in range(int(input())):
    nums += list(map(int, re.findall(r"\d+", input())))
for num in sorted(nums): print(num)
