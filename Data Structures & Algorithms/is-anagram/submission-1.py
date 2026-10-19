class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for s_let in s: 
            if s_let in my_dict: 
                my_dict[s_let] += 1
            else: 
                my_dict[s_let] = 1
        
        my_dict2 = {}
        for t_let in t: 
            if t_let in my_dict2:
                my_dict2[t_let] += 1 
            else: 
                my_dict2[t_let] = 1
        
        return my_dict == my_dict2