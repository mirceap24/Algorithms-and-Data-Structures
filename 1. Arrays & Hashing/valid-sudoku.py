"""
Problem: LeetCode 36 - Valid Sudoku

Key Idea:
To determine if a given Sudoku board is valid, we need to check three conditions:
1. Each row must have distinct digits from 1 to 9.
2. Each column must have distinct digits from 1 to 9.
3. Each 3x3 sub-grid must have distinct digits from 1 to 9.

We can use three nested loops to traverse the entire board and use sets to keep track of digits seen in each row, column, and sub-grid.

Time Complexity:
The time complexity of this approach is O(1), as the Sudoku board is always a fixed 9x9 grid. We traverse each cell of the grid once, and the number of cells is constant.

Space Complexity:
The space complexity is O(1) as well because we are using a fixed amount of additional space (sets) that does not depend on the size of the input grid.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

