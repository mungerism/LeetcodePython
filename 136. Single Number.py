class Solution:
    def singleNumber(self, nums):
        res = 0

        for i in nums:
            res = res ^ i

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([1, 1, 2]))
