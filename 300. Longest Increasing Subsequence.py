"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:

    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        dp = [1 for _ in range(len(nums))]
        longest = 1

        for i in range(1, len(nums)):
            max = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] > max:
                        max = dp[j]
                dp[i] = max + 1
                if dp[i] > longest:
                    longest = dp[i]

        return longest


if __name__ == '__main__':
    solution = Solution()
    res = solution.lengthOfLIS([0])
    print(res)
