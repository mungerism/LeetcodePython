"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target: int):
        self.candidates = candidates
        self.candidates.sort()
        self.results = []
        stack = []
        self.last_candidate = None
        self.dfs(target, stack, 0)

        return self.results

    def dfs(self, remainder, stack, index):

        if remainder == 0:
            self.results.append(stack.copy())
            return

        for i in range(index, len(self.candidates)):

            candidate = self.candidates[i]

            if candidate > remainder:
                return

            if candidate == self.last_candidate:
                continue

            remainder -= candidate

            stack.append(candidate)

            self.dfs(remainder, stack, i + 1)
            remainder += candidate
            self.last_candidate = stack.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
