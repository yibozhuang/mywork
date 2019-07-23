def update(board, m, n, i, j):
    live = 0
    for p in range(max(i - 1, 0), min(i + 2, m)):
        for q in range(max(j - 1, 0), min(j + 2, n)):
            live += board[p][q] & 1

    if live == 3 or live == board[i][j] + 3:
        board[i][j] += 2

def gameOfLife(board):
    if not board or not board[0]:
        return

    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            update(board, m, n, i, j)

    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1

grid = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]


print(grid)
gameOfLife(grid)
print(grid)
