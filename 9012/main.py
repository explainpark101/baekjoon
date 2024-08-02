import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip()
    while "()" in s:
        s = s.replace("()", "")
    if s == "": print("YES")
    else: print("NO")
