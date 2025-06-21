class GameOfLife:
    def gameofLife(self, board: list[list[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                     (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[r][c] for c in range(cols)] for r in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dr, dc in neighbors:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and copy_board[r][c] == 1:
                        live_neighbors += 1

                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                elif copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
