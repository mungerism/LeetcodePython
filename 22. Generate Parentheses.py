"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
	def generateParenthesis(self, n):
		
		results = []
		
		def backtrack(result = '', left = 0, right = 0):
			if left + right == 2 * n:
				results.append(result)
				return 
			
			if left < n:
				backtrack(result + '(', left + 1, right)
			if left > right:
				backtrack(result + ')', left, right + 1)
		
		backtrack()
		return results


if __name__ == '__main__':
	solution = Solution()
	print(solution.generateParenthesis(5))
