from typing import List

class Solution:
    def search(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return matrix[mid]

            elif target < matrix[mid][0]:
                right = mid - 1

            else:
                left = mid + 1
        return False

    def searchMatrix(self, lists, target):
        if not isinstance(lists[0], list):
            return False

        nums = self.search(lists, target)
        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False

