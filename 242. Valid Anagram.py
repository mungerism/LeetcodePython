"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.get_hash_table(s)
        t_map = self.get_hash_table(t)
        return s_map == t_map

    def get_hash_table(self, s):
        map = {}
        for c in s:
            map[c] = map.get(c, 0) + 1
        return map


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('a', 'b'))