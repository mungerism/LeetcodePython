"""
52. N-Queens II

Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.

"""


class Solution:

    # 判断同一列和同一斜线上是否存在 Queue
    def is_valid(self, row, column, queen_record):
        c_left = column
        c_right = column
        for r in range(row, -1, -1):
            if queen_record[r] == column or queen_record[r] == c_left or queen_record[r] == c_right:
                return False
            c_left -= 1
            c_right += 1
        return True

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        chess_board = [['.' for x in range(n)] for y in range(n)]

        # 初始化为 - 1，表示当前行还未放 Queue
        queue_record = [-1 for x in range(n)]
        solutions = []

        row = 0
        column = 0
        has_solution = True
        while has_solution:

            while row in range(n):

                while column < n or queue_record[row] == -1:

                    if column < n and self.is_valid(row, column, queue_record):
                        chess_board[row][column] = 'Q'
                        queue_record[row] = column
                        break
                    else:
                        column += 1

                        if column >= n:
                            # 当前行无法放置 Queue 开始回溯
                            row = row - 1
                            if row < 0:
                                has_solution = False
                                break

                            chess_board[row][queue_record[row]] = '.'
                            column = queue_record[row] + 1
                            queue_record[row] = -1

                if has_solution:
                    column = 0
                    row += 1

            if has_solution:
                solutions.append(chess_board)

                # 回溯
                row -= 1
                chess_board[row][queue_record[row]] = '.'
                column = queue_record[row] + 1
                queue_record[row] = -1

        return len(solutions)


if __name__ == '__main__':
    solution = Solution()
    result = solution.totalNQueens(4)
    print(result)