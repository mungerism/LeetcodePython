"""
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def combinationSum3(self, k: int, n: int):

        self.candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.depth_limit = k
        self.results = []

        stack = []

        self.dfs(n, stack, 0)

        return self.results

    def dfs(self, remainder, stack, index):

        for i in range(index, len(self.candidates)):

            if len(stack) + 1 > self.depth_limit:
                return

            candidate = self.candidates[i]

            if remainder < candidate:
                return

            if remainder == candidate:
                if len(stack) + 1 < self.depth_limit:
                    return

                result = stack.copy()
                result.append(candidate)
                self.results.append(result)
                return

            remainder -= candidate

            stack.append(candidate)
            self.dfs(remainder, stack, i + 1)
            stack.pop()
            remainder += candidate


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))
