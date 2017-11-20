"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        height = len(triangle) + 1
        width = len(triangle[-1]) + 1
        optimal_matrix = [[0 for x in range(width)] for y in range(height)]

        width_range = width - 1
        for h in range(height - 2, -1, -1):
            for w in range(width_range):
                optimal_matrix[h][w] = min(optimal_matrix[h + 1][w], optimal_matrix[h + 1][w + 1]) + triangle[h][w]
            width_range -= 1

        return optimal_matrix[0][0]

if __name__ == '__main__':
    # list = [
    #              [2],
    #             [3,4],
    #            [6,5,7],
    #           [4,1,8,3]
    #         ]

    triangle = [[- 10]]

    solution = Solution()
    print(solution.minimumTotal(triangle))