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
        sub_len = 0
        while right < len(s):
            right_value = s[right]
            if dic.has_key(right_value) and dic[s[]] > left:
                sub_len = right - left
                max_len = max(max_len, sub_len)
                left = dic(s[right]) + 1
                dic[s[right]]=right
            else:
                dic[s[right]]=right
                right += 1
        # sub_len = right - left

        return max_len

if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring('abca')