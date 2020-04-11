"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums)
        mid = int((left + right) / 2)

        first = -1
        last = -1
        target_index = 0

        while left < right:

            if nums[mid] == target:
                target_index = mid
                break
            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
                mid = int((left + right) / 2)
                if mid == left or mid == right:
                    break

        if nums[target_index] == target:
            first = target_index
            last = target_index

            while first > 0 and nums[first - 1] == target:
                first = first - 1

            while last < len(nums) - 1 and nums[last + 1] == target:
                last = last + 1

        return [first, last]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
