"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums) -> int:
        map = {}
        for num in nums:
            if map.get(num) is not None:
                map[num] = map.get(num) + 1
            else:
                map[num] = 1

        majority_value = 0
        majority_key = None
        for key, value in map.items():
            if value > majority_value:
                majority_value = value
                majority_key = key

        return majority_key


if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    print(solution.majorityElement(nums))
