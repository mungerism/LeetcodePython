"""
考点:
1 异或运算交换变量值无需额外空间
2 字符转换为 ASCII 码再进行异或操作
"""


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1

        while i < j:
            s[i] = chr(ord(s[j]) ^ ord(s[i]))
            s[j] = chr(ord(s[i]) ^ ord(s[j]))
            s[i] = chr(ord(s[j]) ^ ord(s[i]))
            i += 1
            j -= 1


if __name__ == '__main__':
    solution = Solution()
    s = ['a', 'b', 'c']
    solution.reverseString(s)
    print(s)
