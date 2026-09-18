class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        path = []

        def backtrack(index):
            # Append current subset
            result.append(path[:])

            # Explore further
            for i in range(index, len(nums)):
                path.append(nums[i])      # choose
                backtrack(i + 1)          # explore
                path.pop()                # un-choose

        backtrack(0)
        return result



