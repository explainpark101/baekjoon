import sys

input = sys.stdin.readline

fib_map = {
    0: {0:1, 1:0},
    1: {0:0, 1:1},
}

def fib_sum(dict1, dict2):
    return {0: dict1[0]+dict2[0], 1: dict1[1]+dict2[1]}

def main():
    for _ in range(int(input())):
        target = int(input())
        for i in range(2, target+1):
            if fib_map.get(i) is None:
                fib_map[i] = fib_sum(fib_map[i-1], fib_map[i-2])
        print(f"{fib_map[target][0]} {fib_map[target][1]}")
    
main()