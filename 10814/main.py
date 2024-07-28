from sys import stdin
from operator import itemgetter

input = stdin.readline
people = ((int(age), name)for age, name in (input().split(" ") for _ in range(int(input()))) if age and name)
people = sorted(people, key=itemgetter(0))
for age, name in people:
    print(age, name, end='')
