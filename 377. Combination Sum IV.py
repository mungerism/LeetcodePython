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

		dp=[1]
		
		for sub_target in range(1, target + 1):
			sum = 0
			for num in nums:
					target_solved = sub_target - num
					if target_solved >= 0:
						sum += dp[target_solved]
			dp.append(sum)
		
		return dp[target]


if __name__ == '__main__':
	solution = Solution()
	print(solution.combinationSum4([1, 2, 3], 6))
