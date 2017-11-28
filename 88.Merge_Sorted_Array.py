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
        i = 0
        j = 0
        while i < m or j < n:

            if nums1[i] < nums2[j]:
                i += 1
            else:
                temp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = temp
                i += 1
            pass


if __name__ == '__main__':
   solution = Solution()
   nums1 = [0, 3, 4]
   nums2 = [1, 2, 5]
   solution.merge(nums1, 3, nums2, 3)


