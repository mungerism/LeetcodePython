"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i = 0
        j = 0
        len_num1 = len(nums1)
        len_num2 = len(nums2)
        while i < len_num1 or j < len_num2:

            if i < len_num1 and j < len_num2:
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            else:
                if i < len_num1:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1

        len_merged = len(merged)
        if len_merged % 2 == 0:
            return (merged[len_merged//2 - 1] + merged[len_merged//2]) / 2
        else:
            return merged[(len_merged + 1)//2 - 1]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
