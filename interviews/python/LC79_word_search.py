import copy

def is_valid_path(board, s0, s1, sub_word):
    if sub_word == "":
        return True

    tmp = board[s0][s1]
    board[s0][s1] = " "
    c = sub_word[0]

    x0 = s0 - 1
    x1 = s1

    if x0 >= 0 and board[x0][x1] == c and is_valid_path(board, x0, x1, sub_word[1:]):
        return True

    x0 = s0
    x1 = s1 - 1

    if x1 >= 0 and board[x0][x1] == c and is_valid_path(board, x0, x1, sub_word[1:]):
        return True

    x0 = s0 + 1
    x1 = s1

    if x0 < len(board) and board[x0][x1] == c and is_valid_path(board, x0, x1, sub_word[1:]):                return True

    x0 = s0
    x1 = s1 + 1

    if x1 < len(board[0]) and board[x0][x1] == c and is_valid_path(board, x0, x1, sub_word[1:]):
        return True

    board[s0][s1] = tmp
    return False

def exist(board, word):
    starting = []
    c0 = word[0]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == c0:
                starting.append((i, j))

    for s in starting:
        if is_valid_path(board, s[0], s[1], word[1:]):
            return True

    return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E'] ]

b = copy.deepcopy(board)
print(exist(b, "ABCCED"))

b = copy.deepcopy(board)
print(exist(b, "SEE"))

b = copy.deepcopy(board)
print(exist(b, "ABCB"))
