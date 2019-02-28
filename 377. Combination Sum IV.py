"""
377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

"""


class Solution:
    def combinationSum4(self, nums, target: int):

        self.nums = nums
        self.nums.sort()
        self.results = []

        self.dfs(target, [])

        return len(self.results)

    def dfs(self, remainder, stack):

        for i in range(0, len(self.nums)):

            num = self.nums[i]

            if remainder == num:
                result = stack.copy()
                result.append(num)
                self.results.append(result)
                return

            if remainder < num:
                return

            remainder -= num
            stack.append(num)

            self.dfs(remainder, stack)
            stack.pop()
            remainder += num


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum4([3, 2, 1], 4))
    print(solution.results)
