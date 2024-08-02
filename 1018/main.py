from sys import stdin


input = stdin.readline
rowMax, colMax = map(int, input().split(" "))
d = {"W": False, "B": True}
board = [
    [ d[color] for color in input().strip() ]
        for _ in range(rowMax)
]
def getChanges(chess_board:list[list[bool]], minimum_changes:int, last_a: bool) -> int:
    changes = 0
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            a, b = chess_board[i][j], chess_board[i][j+1]
            c, d = chess_board[i+1][j], chess_board[i+1][j+1]
            if last_a is not a:
                changes += 1
                a = not a
            if a is b:
                changes += 1
                b = not b
            if a is c:
                changes += 1
                c = not c
            if c is d:
                changes += 1
            last_a = a
            if changes > minimum_changes:
                return minimum_changes
    return changes

minimum_changes = 64
for r_stride in range(rowMax - 7):
    for c_stride in range(colMax - 7):
        chess_board = [row[c_stride: c_stride+8] for row in board[r_stride:r_stride+8]]
        # check minimum changes by 2x2
        for last_a in [True, False]:
            minimum_changes = getChanges(chess_board, minimum_changes, last_a)
print(minimum_changes)
