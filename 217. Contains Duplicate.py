class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = {}
        for num in nums:
            if dic.get(num) is None:
                dic[num] = num
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.containsDuplicate(nums))

    nums1 = [1, 2, 2, 3]
    print(solution.containsDuplicate(nums1))
