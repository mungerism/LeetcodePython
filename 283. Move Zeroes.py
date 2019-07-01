class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        双指针, 指针 i 指向 0, 指针 j 指向非 0 数字
        """
        i = 0
        #找到第一个 0
        while i < len(nums) and nums[i] != 0:
            i += 1

        #开始寻找 0 后面的非 0 数字, 插入到 0 所在的位置
        j = i + 1

        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1



if __name__ == '__main__':
    nums = [0, 1, 5, 0, 3, 0]

    solution = Solution()
    solution.moveZeroes(nums)

    print(nums)



