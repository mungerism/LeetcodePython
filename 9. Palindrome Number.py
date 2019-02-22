"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution:

    # 反转数字
    def reverse(self, x):
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        # 判断反转后是否为位 32 位整数
        return result if result in range(- 2 ** 31, 2 ** 31 - 1) else 0

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数不是回文数
        return True if x == self.reverse(x) and x >= 0 else False


if __name__ == '__main__':

    solution = Solution()
    print(solution.isPalindrome(-2147447412))