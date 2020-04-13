"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution:

    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (i - coins[j] >= 0):
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([2, 5, 10, 1], 27))
