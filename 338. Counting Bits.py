class Solution:
    def countBits(self, num: int):
        count = [0]
        for i in range(1, num + 1):
            last_i = i & (i - 1)
            count.append(count[last_i] + 1)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(3))
