"""
225. Implement Stack using Queues

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_str = self.backspace(S)
        T_str = self.backspace(T)
        print(S_str)
        print(T_str)
        return S_str == T_str

    def backspace(self, S):
        queue_s = []
        for s in S:
            if s == '#':
                if queue_s:
                    queue_s.pop()
            else:
                queue_s.append(s)
        return ''.join(queue_s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare("ab#b", "#ad#b"))
