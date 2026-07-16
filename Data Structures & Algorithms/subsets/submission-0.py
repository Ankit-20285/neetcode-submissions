class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, current):

            if index == len(nums):
                result.append(current[:])   # Store a copy
                return

            # Include nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)

            # Remove it (backtrack)
            current.pop()

            # Exclude nums[index]
            backtrack(index + 1, current)

        backtrack(0, [])
        return result