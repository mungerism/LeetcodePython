"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:

    def is_valid(self, column, row, queue_record):
        r_left = row
        r_right = row
        for c in range(column, -1, -1):
            if queue_record[c] == row or queue_record[c] == r_left or queue_record[c] == r_right:
                return False
            r_left -= 1
            r_right += 1

        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = [['.' for x in range(n)] for y in range(n)]
        queue_record = [-1 for x in range(n)]
        solutions = []

        c = 0
        r = 0
        has_solution = True
        while has_solution:

            while c < n and c > -1:

                while r < n or queue_record[c] == -1:

                    if  r < n and self.is_valid(c, r, queue_record):
                        board[c][r] = 'Q'
                        queue_record[c] = r
                        break
                    else:
                        r += 1
                        if r >= n:
                            c = c - 1

                            if c < 0:
                                has_solution = False
                                break

                            board[c][queue_record[c]] = '.'
                            r = queue_record[c] + 1
                            queue_record[c] = -1

                if has_solution:
                    r = 0
                    c += 1

            if has_solution:
                solution = []
                for e in board:
                    solution.append( "".join(e))

                solutions.append(solution)
                c = n - 1
                board[c][queue_record[c]] = '.'
                r = queue_record[c] + 1
                queue_record[c] = -1

        return solutions

if __name__ == '__main__':
    solution = Solution()
    result = solution.solveNQueens(4)
