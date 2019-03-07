"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution:
    def topKFrequent(self, nums, k: int):

        dic = {}

        for num in nums:

            if dic.get(num) is None:
                dic[num] = 1
            else:
                dic[num] += 1

        sorted_by_value = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_by_value[i][0])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4], 2))
