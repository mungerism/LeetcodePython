class Solution:
    def maxProduct(self, nums) -> int:
        max_result = nums[0]
        min_result = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            new_max_result = max(max_result * num, min_result * num, num)
            min_result = min(max_result * num, min_result * num, num)
            max_result = new_max_result
            result = max(max_result, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([-1, -2, -9, -6]))
