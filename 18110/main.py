from sys import stdin
from typing import Iterable, Union
def round(num: float) -> int:
    q, r = divmod(num, 1)
    return int(q + int(r+0.5))
def mean(l:Iterable[Union[int, float]]) -> float:
    return sum(l) / len(l)

input = stdin.readline

def main():
    n = int(input())
    if n == 0:
        return print(0)
    cut = round(n * .15)
    ratings = sorted(map(int, (input() for _ in range(n))))
    if cut != 0:
        ratings = ratings[cut:-cut]
    print(round(mean(ratings)))

main()