"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''

        result = strs[0]

        for str in strs:
            result = self.commonPrefix(result, str)
        return result

    def commonPrefix(self, str, str1):
        commonPrefix = ''
        size = len(str) if len(str) <= len(str1) else len(str1)
        for i in range(size):
            if str[i] == str1[i]:
                commonPrefix = commonPrefix + str[i]
            else:
                break
        return commonPrefix


if __name__ == '__main__':
    solution = Solution()
    strs = ['abcdee', 'abcde', 'abcd']
    print(solution.longestCommonPrefix(strs))
