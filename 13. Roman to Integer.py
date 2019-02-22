"""
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = dic[s[0]]

        for i in range(1, len(s)):
            result = result + dic[s[i]]
            if dic[s[i]] > dic[s[i - 1]]:
                result = result - 2 * dic[s[i - 1]]

        return result


if __name__ == '__main__':

    solution = Solution()
    print(solution.romanToInt("MCMXCVI"))
    # print(solution.romanToInt("IV"))