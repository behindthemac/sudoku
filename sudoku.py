import copy


class Sudoku:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def get_solutions(self, n=0):
        """Generates all possible solutions of a Sudoku puzzle.

        Yields:
            The solutions of a Sudoku puzzle
        """
        if n < 9 ** 2:
            row = n // 9
            col = n % 9
            if self.grid[row][col] is None:
                for num in range(1, 10):
                    if self.is_valid(row, col, num):
                        self.grid[row][col] = num
                        yield from self.get_solutions(n + 1)
                        self.grid[row][col] = None
            else:
                yield from self.get_solutions(n + 1)
        else:
            yield self.grid

    def is_valid(self, row, col, num):
        """Checks if the placement is valid or not.

        Args:
            row: The index of the row where the number is placed.
            col: The index of the column where the number is placed.
            num: The number which is placed.

        Returns:
            True if the placement is valid, False otherwise.
        """
        if num in self.get_row(row):
            return False

        if num in self.get_col(col):
            return False

        box = (row // 3) * 3 + (col // 3)
        if num in self.get_box(box):
            return False

        return True

    def get_row(self, row):
        """Gets the elements on the specified row.

        Args:
            row: The index of the row whose elements are returned.

        Returns:
            The elements on the specified row.
        """
        return self.grid[row]

    def get_col(self, col):
        """Gets the elements on the specified column.

        Args:
            col: The index of the column whose elements are returned.

        Returns:
            The elements on the specified column.
        """
        return [self.grid[row][col] for row in range(9)]

    def get_box(self, box):
        """Gets the elements on the specified subgrid.

        Args:
            box: The index of the subgrid whose elements are returned.

        Returns:
            The elements on the specified subgrid.
        """
        r = (box // 3) * 3
        c = (box % 3) * 3
        return [self.grid[row][col] for row in range(r, r + 3) for col in range(c, c + 3)]
