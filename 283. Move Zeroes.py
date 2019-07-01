class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                z = z + 1
                n = 1
                while j < len(nums) - z:

                    while 

                    nums[j] = nums[j + 1]
                    j = j + 1

        for m in range(-1, -(z + 1), -1):
            print(m)
            nums[m] = 0


if __name__ == '__main__':
    nums = [0]

    solution = Solution()
    solution.moveZeroes(nums)

    print(nums)



