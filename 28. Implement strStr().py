"""
28. Implement strStr().py

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""

class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		
		if not needle:
			return 0
		
		for i in range(len(haystack)):
			
			if i + len(needle) > len(haystack):
				return -1
			
			if haystack[i] == needle[0]:
				is_part_of = True
				for j in range(1, len(needle)):
					if needle[j] != haystack[i + j]:
						is_part_of = False
				if is_part_of:
					return i
		return -1
		
		
if __name__ == '__main__':
	solution = Solution()
	print(solution.strStr('a', 'a'))
