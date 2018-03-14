"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {'(': ')', '[': ']', '{': '}'}
        set = ['(', '[', '{']

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in set:
                stack.append(c)
            else:
                if not stack or dic[stack.pop()] != c:
                    return False
        return not stack

if __name__ == '__main__':

    solution = Solution()
    print(solution.isValid('(('))
