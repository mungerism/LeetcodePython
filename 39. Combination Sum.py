"""
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:

    def combinationSum(self, candidates, target: int):
        self.results = []
        self.candidates = candidates
        self.target = target
        self.candidates.sort()

        self.dfs(target, [], 0)

        return self.results

    def dfs(self, remainder, stack, index):
        if remainder == 0:
            self.results.append(stack.copy())
            return

        if remainder < 0:
            return

        for i in range(index, len(self.candidates)):

            candidate = self.candidates[i]

            if candidate > remainder:
                return

            remainder -= candidate
            stack.append(candidate)

            self.dfs(remainder, stack, i)

            stack.pop()
            remainder += candidate


if __name__ == '__main__':
    solution = Solution()
    print((solution.combinationSum([3, 2, 6, 7, 8, 9], 7)))
