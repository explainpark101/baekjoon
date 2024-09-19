from functools import cache
import sys
from math import isqrt
input = sys.stdin.readline

@cache
def count_prime_factors(n: int, count = 1) -> int:
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return count_prime_factors(n // i, count+1)
    return count

@cache
def is_prime(n: int) -> bool:
    if n == 1: return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return True

def main():
    a, b = map(int, input().split(" "))
    print(sum(
        1 for _ in range(a, b+1) if is_prime(count_prime_factors(_))
    ))

if __name__ == "__main__":
    main()