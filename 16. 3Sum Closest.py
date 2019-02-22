"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        size = len(nums)
        dic = {}
        arr = []
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = size - 1

            diff = 0
            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                if right < size - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                s = nums[left] + nums[right] + nums[i]
                diff = s - target
                if diff == 0:
                    return nums[left] + nums[right] + nums[i]
                else:
                    if abs(diff) not in dic:
                        dic[abs(diff)] = [nums[left], nums[right], nums[i]]
                        arr.append(abs(diff))

                    if diff > 0:
                        right -= 1
                    else:
                        left += 1

        arr.sort()
        return (dic[arr[0]][0] + dic[arr[0]][1] + dic[arr[0]][2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([0, 1, 2], 3))
