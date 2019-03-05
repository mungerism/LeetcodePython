"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:

    def fourSum(self, nums, target):

        results = []
        nums.sort()

        for i in range(len(nums) - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1

                right = len(nums) - 1

                while left < right:
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue

                    if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue

                    result = nums[i] + nums[j] + nums[left] + nums[right]

                    if result == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                    if result < target:
                        left += 1

                    if result > target:
                        right -= 1

        return results

    # 递归超时了
    # def fourSum2(self, nums, target: int):
    #
    #     self.results = []
    #     self.last_num = None
    #     self.nums = nums
    #     self.nums.sort()
    #     #		print(self.nums)
    #     self.dfs(target, [], 0)
    #     return self.results
    #
    # def dfs(self, target, stack, index):
    #
    #     for i in range(index, len(self.nums)):
    #
    #         num = self.nums[i]
    #
    #         if self.last_num == num:
    #             continue
    #
    #         # print( 'i', i, 'num', num, 'stack', stack)
    #
    #         if len(stack) > 3:
    #             return
    #
    #         if target > 0 and target - num < 0:
    #             return
    #
    #         if target < 0 and target - num > 0:
    #             return
    #
    #         if target == num and len(stack) == 3:
    #             result = stack[:]
    #             result.append(num)
    #             # print('res', result)
    #             self.results.append(result)
    #             return
    #
    #         stack.append(num)
    #         target -= num
    #
    #         self.dfs(target, stack, i + 1)
    #         self.last_num = stack.pop()
    #         target += num


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 0, -1, 0, -2, 2]
    # nums = [-3,-1,0,2,4,5]
    print(solution.fourSum(nums, 0))
