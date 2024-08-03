from math import sqrt
from sys import stdin
from typing import Generator, Iterable, TypeVar
T1 = TypeVar("T1")
T2 = TypeVar("T2")
def zip_short(iter1: Iterable[T1], iter2: Iterable[T2]) -> Generator[tuple[T1, T2], None, None]:
    if len(iter1) >= len(iter2):
        return ((iter1[i], i2) for i, i2 in enumerate(iter2) )
    return ((i1, iter2[i]) for i, i1 in enumerate(iter1) )
input = stdin.readline

row, col = map(int, input().split(" "))
nums = [
    input().strip() for _ in range(row)
]
res = set()
maximum = -1

dx_list: list[range] = [
        [i for _ in range(col)] for i in range(row)
    ] + list(
        set((range(i, row-j, dx) for dx in range(1, row) for i in range(row) for j in range(row))) |
        set((range(row-j-1, i-1, -dx) for dx in range(1, row) for i in range(row) for j in range(row)))
    )

dy_list: list[range] = [
        [i for _ in range(row)] for i in range(col)
    ] + list(
        set((range(i, col-j, dy) for dy in range(1, col) for i in range(col) for j in range(col))) |
        set((range(col-j-1, i-1, -dy) for dy in range(1, col) for i in range(col) for j in range(col)))
    )

for dxl in dx_list:
    for dyl in dy_list:
        num = ""
        for i, j in zip_short(dxl, dyl):
            num += nums[i][j]
            val = int(num)
            if val in res or sqrt(val) % 1 and val != 0: continue
            res.add(val)
            maximum = max(maximum, val)

print(maximum)
