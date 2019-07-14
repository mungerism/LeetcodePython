import sys


class Solution:
    def maxProfit(self, prices) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
