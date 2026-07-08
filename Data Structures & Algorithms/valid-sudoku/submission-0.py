class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()

            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check Columns
        for col in range(9):
            seen = set()

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check 3x3 Boxes
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):

                seen = set()

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):

                        value = board[row][col]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True