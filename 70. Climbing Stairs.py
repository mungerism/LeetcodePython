class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n is 1 or n is 2:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(10))