"""
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        return self.permute(nums)

    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        results = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            remain_nums = nums[: i] + nums[i + 1:]
            for result in self.permute(remain_nums):
                result.append(num)
                results.append(result)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 3]))
