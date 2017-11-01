"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        left = 0
        right = 0
        dic = {}
        while right < len(s):
            right_value = s[right]
            if dic.has_key(right_value) and dic[right_value] >= left:
                sub_len = right - left
                max_len = max(max_len, sub_len)
                left = dic[right_value] + 1
                dic[right_value]=right
                right += 1
            else:
                dic[right_value]=right
                right += 1
                sub_len = right - left
                max_len = max(max_len, sub_len)

        return max(max_len, sub_len)

if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring('abcabcbb')