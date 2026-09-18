class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, value in enumerate(nums):
            second_num = target - value
            if second_num in seen:
                return [min(i, seen[second_num]), max(seen[second_num], i)]
            seen[value] = i 

        return None
