BATTLESHIP = "X"

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:

    def is_in_bounds(self, board, row, col):

        num_rows = len(board)
        num_cols = len(board[0])

        row_in_bounds = row >= 0 and row < num_rows
        col_in_bounds = col >= 0 and col < num_cols

        return row_in_bounds and col_in_bounds
        
    def mark_current_battleship(self, board, visited, row, col):

        if not self.is_in_bounds(board, row, col):
            return
        
        if (row, col) in visited:
            return
        
        if board[row][col] != BATTLESHIP:
            return 

        visited.add((row, col))

        for row_offset, col_offset in directions:
            new_row = row + row_offset
            new_col = col + col_offset

            self.mark_current_battleship(board, visited, new_row, new_col)

    def countBattleships(self, board: List[List[str]]) -> int:

        num_rows = len(board)
        num_cols = len(board[0])

        visited = set()

        num_battleships = 0

        for row in range(num_rows):
            for col in range(num_cols):

                if board[row][col] == BATTLESHIP and (row, col) not in visited:
                    self.mark_current_battleship(board, visited, row, col)
                    num_battleships += 1

        return num_battleships