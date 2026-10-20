class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)
        right = 1
        
        for i in range(1, len(ans)):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        for j in range(len(ans) - 2, -1, -1): 
            right *= nums[j + 1]
            ans[j] *= right
            
        return ans