"""
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:

    def threeSum(self, nums):
        result = []
        nums.sort()
        size = len(nums)

        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1

            right = size - 1

            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                if right < size - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    right -= 1
                    left += 1
                else:
                    if s > 0:
                        right -= 1
                    else:
                        left += 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
