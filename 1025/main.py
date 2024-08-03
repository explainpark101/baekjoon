import math


rowCount, colCount = map(int, input().split(" "))
tbl = [
    input().strip() for _ in range(rowCount)
]

res = set()
answer = -1
for row in range(rowCount):
    for col in range(colCount):
        for dx in range(-row, row):
            for dy in range(-col, col):
                if dx == dy == 0: continue
                s = ""
                n, m = row, col
                while (0 <= n < rowCount) and (0 <= m < colCount):
                    s += tbl[n][m]
                    val = int(s)
                    n += dx
                    m += dy

                    if val in res: continue
                    if math.sqrt(val) % 1: continue
                    answer = max(answer, val)
                    res.add(val)
print(answer)
