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
        width = len(grid[0])

        optimal_matrix = [[0 for x in range(width)] for y in range(height)]

        for w in range(width):
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

        return optimal_matrix[height - 1][width - 1]

if __name__ == '__main__':

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    solution = Solution()
    print(solution.minPathSum(grid))
"""宝宝写的
class Solution:
    def minPathSum(self, grid):
      
        height = len(grid)
        width  = len(grid[0])
        arr = [[0 for x in range(width)] for y in range(height)]
        for h in range(height):
            for w in range(width):
                if h == 0 and w==0:
                    arr[h][w] = grid[0][0]
                elif h==0 and w > 0:
                    print("w", w, "h", h)
                    arr[h][w] = grid[h][w]+arr[h][w-1]
                elif w == 0 and h > 0:
                    arr[h][w] = grid[h][w]+arr[h-1][w]
                else:
                    arr[h][w] = grid[h][w]+min(arr[h][w-1],arr[h-1][w])
        return (arr[height-1][width-1])
if __name__ == '__main__':
    solution = Solution()
    arr = [[1,2,5],[3,2,1]]
    solution.minPathSum(arr)
"""