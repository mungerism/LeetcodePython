class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left + right) // 2

        while target != nums[mid]:
            if nums[left] > nums[mid]:
                mid = (mid - 1 + left) // 2
            else:
                mid = (mid + 1 + right) // 2


if __name__ == '__main__':
    solution = Solution()
    print(5 / 2)

    print(solution.search([4, 5, 6, 7, 0, 1, 2], ))
