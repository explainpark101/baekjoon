import sys

input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return pow(x1-x2, 2) + pow(y1-y2, 2)

def main():
    test_case_count:int = int(input())
    for t in range(test_case_count):
        x1, y1, x2, y2 = list(map(int, input().split(" ")))
        start = x1, y1
        end = x2, y2
        
        entry_count = 0
        
        planet_count:int = int(input())

        # cx, cy, r
        planets = (list(map(int, input().split(" "))) for p in range(planet_count))
        for *planet_coord,r in planets:
            starting = dist(*start, *planet_coord) < pow(r, 2)
            ending = dist(*end, *planet_coord) < pow(r, 2)
            if starting != ending:
                entry_count += 1
        print(entry_count)

main()
            