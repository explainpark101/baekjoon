import sys, re
input = sys.stdin.readline

itercount = int(input())
regexp = input().strip()
for i in range(itercount):
    print("DA" if re.search("^"+regexp.replace("*", ".*")+"$", input().strip()) is not None else "NE")