"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        optimal_matrix = [x for x in range(len(s))]

        for i in range(1, len(s)):
            optimal_matrix[i] = optimal_matrix[i - 1] + 1
            for j in range(i):
                sub_s = s[j : i + 1]
                if sub_s == sub_s[ : :-1]:
                    if j == 0:
                        optimal_matrix[i] = 0
                    else:
                        optimal_matrix[i] = min(optimal_matrix[j - 1] + 1, optimal_matrix[i])

        return optimal_matrix[len(s) - 1]
                

if __name__ == '__main__':
    solution = Solution()
    print (solution.minCut("cdd"))

