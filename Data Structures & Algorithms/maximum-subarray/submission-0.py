class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        best = nums[0]

        for num in nums[1:]: 
            curr = max(num, curr + num) 
            best = max(curr, best)
        
        return best

