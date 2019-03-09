"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		result = '0'
		for i in reversed(range(len(num2))):
			sub_result = self.simple_multiply(num1, num2[i], len(num2) - i - 1)

			result = self.add_nums(result, sub_result)

		return result

	def simple_multiply(self, num1, num2, i):

		if num2 == '0' or num1 == '0':
			return '0'

		result = ''
		quotient = 0
		for j in reversed(range(len(num1))):
			product = int(num1[j]) * int(num2) + quotient
			quotient = product // 10
			remainder = product % 10
			result = str(remainder) + result

		if quotient != 0:
			result = str(quotient) + result

		for k in range(i):
			result += '0'
		
		return result

	def add_nums(self, num1, num2):

		#print('add', 'num1', num1, 'num2', num2)
		quotient = 0
		result = ''

		size = max(len(num1), len(num2))

		for i in range(-1, -size - 1, -1):

			if i * -1 < len(num1) + 1:
				n1 = num1[i]
			else:
				n1 = 0

			if i * -1 < len(num2) + 1:
				n2 = num2[i]
			else:
				n2 = 0

			sum_result = int(n1) + int(n2) + quotient
			quotient = sum_result // 10
			remainder = sum_result % 10
			result = str(remainder) + result
		
		if quotient > 0:
			result = str(quotient) + result
		
		return result


if __name__ == '__main__':
	solution = Solution()
	# print(solution.simple_multiply('123', '10', 0))
	#print(solution.add_nums('111', '111919'))
	
	num1 = '123456789'
	num2 = '987654321'
	res = '121932631112635269'
	print(solution.multiply(num1, num2))
