class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = {}

        for i in nums: 
            if i not in my_dict: 
                my_dict[i] = 1 
            else: 
                my_dict[i] += 1 
            
        for key, values in my_dict.items(): 
            if values >= 2: 
                return key 
        