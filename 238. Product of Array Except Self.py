"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):

        res = []
        res.append(1)

        for i in range(1, len(nums)):
            res.append(nums[i - 1] * res[i - 1])

        print(res)

        last_right_product = 1
        for i in reversed(range(len(nums) - 1)):
            res[i] = res[i] * nums[i + 1] * last_right_product
            last_right_product = last_right_product * nums[i + 1]

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf(nums=[1, 2, 3, 4]))
