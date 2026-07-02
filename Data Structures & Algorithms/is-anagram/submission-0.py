class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        my_dict2 = {}
        for i in s: 
            if i not in my_dict: 
                my_dict[i] = 1 
            else: 
                my_dict[i] += 1
        for j in t: 
            if j not in my_dict2: 
                my_dict2[j] = 1 
            else: 
                my_dict2[j] += 1
        
        if my_dict == my_dict2: 
            return True 

        return False 
        