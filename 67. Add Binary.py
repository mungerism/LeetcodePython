"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        result, carry, value = "", 0, 0
        for i in range(max(len(a), len(b))):
            if i >= len(a):
                value = int(b[-(i + 1)])
            elif i >= len(b):
                value = int(a[-(i + 1)])
            else:
                value = int(a[-(i + 1)]) + int(b[-(i + 1)])
            value += carry
            carry = value // 2
            result = str(value % 2) + result

        if carry > 0:
            result = str(carry) + result

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11", "1"))
