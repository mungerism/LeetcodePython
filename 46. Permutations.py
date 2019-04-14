"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        results = []

        for i, num in enumerate(nums):
            remain_nums = nums[: i] + nums[i + 1:]
            for result in self.permute(remain_nums):
                result.append(num)
                results.append(result)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
