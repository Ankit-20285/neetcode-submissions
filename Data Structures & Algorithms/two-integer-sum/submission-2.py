class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        ans = []

        for i in range(len(nums)): 
            if target - nums[i] in my_dict: 
                ans.append(nums.index(target - nums[i]))
                ans.append(i)
            if nums[i] not in my_dict: 
                my_dict[nums[i]] = i
        
        return ans
            
