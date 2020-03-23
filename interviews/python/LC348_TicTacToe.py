class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0


    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        player_value = 1
        if player == 2:
            player_value = -1

        return_value = 0

        self.rows[row] += player_value
        self.cols[col] += player_value

        if row == col:
            self.diag1 += player_value
            if abs(self.diag1) == self.n:
                return player

        if (self.n - 1 - row) == col:
            self.diag2 += player_value
            if abs(self.diag2) == self.n:
                return player

        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n:
            return player

        return return_value


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
