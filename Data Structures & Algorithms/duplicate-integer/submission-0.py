class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for i in nums: 
            if i not in my_dict: 
                my_dict[i] = 1
            else: 
                my_dict[i] += 1 

        for i in my_dict.values(): 
            if i >= 2: 
                return True 
        
        return False