class Solution:
    def search(self, nums, target: int) -> int:

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        if nums[left] > nums[right]:
            while nums[mid] < nums[mid + 1]:
                if nums[left] < nums[mid]:
                    left = mid
                    mid = (left + right) // 2
                else:
                    right = mid
                    mid = (left + right) // 2

            rotated_index = mid + 1
            left = 0
            right = len(nums) - 1

            if target >= nums[left]:
                right = rotated_index - 1
                mid = (left + right) // 2
            else:
                left = rotated_index
                mid = (left + right) // 2

        while target != nums[mid]:
            if target < nums[mid]:
                right = mid - 1
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2

            if left > right:
                return -1

        return mid


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 1, 2, 3], 1))
