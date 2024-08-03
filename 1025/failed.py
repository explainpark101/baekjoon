from math import sqrt
from sys import stdin
from typing import Iterable, Literal
input = stdin.readline
def zip_short(iter1: Iterable, iter2: Iterable):
    if len(iter1) >= len(iter2):
        return ((iter1[i], i2) for i, i2 in enumerate(iter2) )
    return ((i1, iter2[i]) for i, i1 in enumerate(iter1) )

row, col = map(int, input().split(" "))
nums = [
    input().strip() for _ in range(row)
]
def check_maximum(nums:list[str], row:int, col:int, maximum:int, res = set()) -> tuple[int, set]:
    if len(nums) == 0 or len(nums[0]) == 0: return maximum, res
    for dx in range(0, row):
        for dy in range(0, col):
            if dx == dy == 0:
                numbers = set()
                for r in nums:
                    for i in r:
                        numbers.add(i)
                numbers = set(map(int, numbers))
                if 0 in numbers:
                    maximum = max(maximum, 0)
                for num in numbers:
                    if num in res: continue
                    if sqrt(num) % 1: continue
                    maximum = max(maximum, num)
                    res.add(num)
                continue
            if dx == 0:
                for i in range(row):
                    for num in (
                        int("".join(nums[i][j] for j in range(0, col, dy))),
                        int("".join(nums[i][j] for j in range(col-1, -1, -dy)))
                    ):
                        if num in res: continue
                        if sqrt(num) % 1: continue
                        maximum = max(maximum, num)
                        res.add(num)
                        continue
                continue
            if dy == 0:
                for j in range(col):
                    for num in (
                        int("".join(nums[i][j] for i in range(0, row, dx))),
                        int("".join(nums[i][j] for i in range(row-1, -1, -dx))),
                    ):
                        if num in res: continue
                        if sqrt(num) % 1: continue
                        maximum = max(maximum, num)
                        res.add(num)
                        continue
                continue
            for num in (
                int("".join((nums[i][j] for i,j in zip_short(range(0, row, dx), range(0, col, dy))))),
                int("".join((nums[i][j] for i,j in zip_short(range(row-1, -1, -dx), range(col-1, -1, -dy))))),
                int("".join((nums[i][j] for i,j in zip_short(range(0, row, dx), range(col-1, -1, -dy))))),
                int("".join((nums[i][j] for i,j in zip_short(range(row-1, -1, -dx), range(0, col, dy)))))
            ):
                if sqrt(num) % 1: continue
                maximum = max(maximum, num)
                res.add(num)
    return maximum, res

res = set()
maximum = -1
for skip_x in range(row):
    for skip_y in range(col):
        _row = row-skip_x
        _col = col-skip_y
        nums_copy = [r[skip_y:] for r in nums[skip_x:]]
        if len(nums_copy) == 0 or len(nums_copy[0]) == 0: continue
        maximum, res = check_maximum(nums_copy, _row, _col, maximum)

        if skip_x + skip_y == 0: continue
        nums_copy = [r[:-skip_y] for r in nums[skip_x:]]
        maximum, res = check_maximum(nums_copy, _row, _col, maximum)

        nums_copy = [r[skip_y:] for r in nums[:-skip_x]]
        maximum, res = check_maximum(nums_copy, _row, _col, maximum)

        nums_copy = [r[:-skip_y] for r in nums[:-skip_x]]
        maximum, res = check_maximum(nums_copy, _row, _col, maximum)

        # 양쪽 자르기
        nums_copy = [r[skip_y:-skip_y] for r in nums[:-skip_x]]
        maximum, res = check_maximum(nums_copy, _row, _col-skip_y, maximum)

        nums_copy = [r[:-skip_y] for r in nums[skip_x:-skip_x]]
        maximum, res = check_maximum(nums_copy, _row-skip_x, _col, maximum)

        nums_copy = [r[skip_y:-skip_y] for r in nums[skip_x:-skip_x]]
        maximum, res = check_maximum(nums_copy, _row-skip_x, _col-skip_y, maximum)
print(maximum)
