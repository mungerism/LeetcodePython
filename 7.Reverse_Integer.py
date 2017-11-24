"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(str(x)[::-1]) if x >= 0 else int('-'+str(x)[:0:-1])

        # 32 位 int 类型的范围，第一位为符号位
        return result if result in range(- 2 ** 31, 2 ** 31 -1) else 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))