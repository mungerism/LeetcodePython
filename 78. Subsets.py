"""
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:

    def __init__(self):
        self.results = None

    def dfs(self, nums, stack, index):

        if index == len(nums):
            return

        for i in range(index, len(nums)):
            stack.append(nums[i])
            self.dfs(nums, stack, i + 1)
            self.results.append(stack.copy())
            stack.pop()

    def subsets(self, nums):
        self.results = [[]]
        self.dfs(nums, [], 0)
        return self.results


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))