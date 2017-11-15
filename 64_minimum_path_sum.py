"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        height = len(grid)
        weight = len(grid[0])

        optimal_matrix = [[0 for x in range(weight)] for y in range(height)]

        for w in range(weight):
            for h in range(height):

                if w == 0 or h == 0:
                    if w == 0 and h >= 1:
                        optimal_matrix[h][w] = optimal_matrix[h - 1][w] + grid[h][w]
                    elif h == 0 and w >= 1:
                        optimal_matrix[h][w] = optimal_matrix[h][w - 1] + grid[h][w]
                    else:
                        optimal_matrix[h][w] = grid[h][w]
                else:
                    optimal_matrix[h][w] = min(optimal_matrix[h - 1][w], optimal_matrix[h][w - 1]) + grid[h][w]

        return optimal_matrix[height - 1][weight - 1]

if __name__ == '__main__':

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    solution = Solution()
    print(solution.minPathSum(grid))
