class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1 
            
        for key, value in my_dict.items(): 
            if value >= 2: 
                return True
        
        return False