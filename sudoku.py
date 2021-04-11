class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def solve(self, n=0):
        if n < 9 ** 2:
            row = n // 9
            col = n % 9
            if self.grid[row][col] is None:
                for val in range(1, 10):
                    if self.validate(row, col, val):
                        self.grid[row][col] = val
                        yield from self.solve(n + 1)
                        self.grid[row][col] = None
            else:
                yield from self.solve(n + 1)
        else:
            yield self.grid

    def validate(self, row, col, val):
        if val in self.get_row(row):
            return False

        if val in self.get_col(col):
            return False

        box = (row // 3) * 3 + col // 3
        if val in self.get_box(box):
            return False

        return True

    def get_row(self, row):
        return self.grid[row]

    def get_col(self, col):
        return [self.grid[row][col] for row in range(9)]

    def get_box(self, box):
        r = (box // 3) * 3
        c = (box % 3) * 3
        return [self.grid[row][col] for row in range(r, r + 3) for col in range(c, c + 3)]
