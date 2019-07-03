class Solution:

    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if self.dic.get(n):
            return self.dic.get(n)

        self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dic[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(35))
