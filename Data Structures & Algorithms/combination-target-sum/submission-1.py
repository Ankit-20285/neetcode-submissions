class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, path, target): 
            if target == 0: 
                ans.append(path.copy())
                return 

            for i in range(start, len(nums)): 
                remain = target - nums[i]
                if remain >= 0: 
                    path.append(nums[i]) 
                    backtrack(i, path, remain)
                    path.pop() 

        backtrack(0, [], target) 
        return ans