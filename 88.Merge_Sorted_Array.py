"""
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # 从后往前比较两个数组的元素

        merged = m + n - 1
        m = m - 1
        n = n - 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[merged] = nums1[m]
                m -= 1
            else:
                nums1[merged] = nums2[n]
                n -= 1
            merged -= 1

        if m < 0:
            nums1[:n + 1] = nums2[:n + 1]



if __name__ == '__main__':
   solution = Solution()
   nums1 = [1, 2, 3, 0, 0, 0]
   nums2 = [2, 5, 6]
   solution.merge(nums1, 3, nums2, 3)


