class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(111101))
