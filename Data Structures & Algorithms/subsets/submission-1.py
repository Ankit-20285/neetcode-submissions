class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(index, path):
            result.append(path.copy())

            for i in range(index, len(nums)): 
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop() 
            
        
        backtrack(0, [])

        return result