class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        res = ''
        s = s + ' '

        for c in s:

            if c is ' ':
                while stack:
                    res = res + stack.pop()
                res = res + ' '
            else:
                stack.append(c)

        return res[0:-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))
