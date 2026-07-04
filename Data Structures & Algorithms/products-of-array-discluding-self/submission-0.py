class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        multi = 1 

        for i in range(len(nums)): 
            for j in range(len(nums)): 
                if j != i: 
                    multi *= nums[j]
            
            answer.append(multi)
            multi = 1
        
        return answer