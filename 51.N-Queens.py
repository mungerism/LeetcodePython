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
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = [['.' for x in range(n)] for y in range(n)]
        back_tracking = [-1 for x in range(n)]
        solutions = []

        c = 0
        r = 0

        while True:
            while c < n:

                while r < n or back_tracking[c] == -1:

                    if  r < n and isValid(c, r, board):
                        board[c][r] = 'Q'
                        back_tracking[c] = r
                        break
                    else:
                        r += 1
                        if r >= n:
                            c = c - 1
                            board[c][back_tracking[c]] = '.'
                            r = back_tracking[c] + 1
                            back_tracking[c] = -1
                r = 0
                c += 1

            solution = board
            solutions.append(solution)
            r += 1
            c -= 1


def isValid(c, r, board):
    for i in range(c, -1, -1):
        if board[i][r] == 'Q':
            return False

    i = c
    j = r
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = c
    j = r
    while i >= 0 and j < len(board[0]):
        print("i", i, "j", j)
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

if __name__ == '__main__':
    solution = Solution()
    solution.solveNQueens(4)