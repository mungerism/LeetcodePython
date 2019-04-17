"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        self.results = [[]]
        self.dfs(nums, [], 0)
        return self.results

    def dfs(self, nums, stack, index):
        if index == len(nums):
            return
        i = index
        while i < len(nums):
            stack.append(nums[i])
            self.dfs(nums, stack, i + 1)
            self.results.append(stack.copy())
            print(stack)
            stack.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([5, 5, 5, 5, 5]))