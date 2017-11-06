"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        table = [[0 for x in range(length)] for y in range(length)]
        start = 0
        max_len = 0

        for sub_len in range(1, length + 1):

            for left in range(length - sub_len + 1):
                right = left + sub_len - 1

                if sub_len == 1:
                    table[left][right] = sub_len
                    start = left
                    max_len = sub_len
                elif sub_len == 2:
                    if s[left] == s[right]:
                        table[left][right] = sub_len
                        start = left
                        max_len = sub_len
                    else:
                        table[left][right] = 0
                else:
                    prev_len = table[left + 1][right - 1]
                    if prev_len > 0 and s[left] == s[right]:
                        table[left][right] = prev_len + 2
                        start = left
                        max_len = sub_len
                    else:
                        table[left][right] = 0

        max_str = s[start: start + max_len]

        return max_str

if __name__ == '__main__':
    solution = Solution()
    print solution.longestPalindrome('sweaa')
