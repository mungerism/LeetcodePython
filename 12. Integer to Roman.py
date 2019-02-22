"""
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        result = ""

        while i < len(integers):
            if num >= integers[i]:
                result = result + romans[i]
                num = num - integers[i]
                i -= 1

            i += 1

        return result


if __name__ == '__main__':

    solution = Solution()
    print(solution.intToRoman(2))