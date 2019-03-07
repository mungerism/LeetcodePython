"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution:

    def quick_sort(self, start, end, arr):

        if start >= end:
            return

        pivot = arr[start]
        left = start
        right = end

        while left < right:

            while arr[right] > pivot and left < right:
                right -= 1

            while arr[left] <= pivot and left < right:
                left += 1

            arr[left], arr[right] = arr[right], arr[left]

        arr[start], arr[right] = arr[right], arr[start]

        self.quick_sort(start, right - 1, arr)
        self.quick_sort(right + 1, end, arr)

        return


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_sort(0, len(nums)-1, nums)
        return nums[len(nums) - k]


if __name__ == '__main__':

    # nums = [3,2,3,1,2,4,5,5,6]
    # nums = [2, 1, 3]
    nums = [2, 1]
    solution = Solution()
    print(solution.findKthLargest(nums, 1))
