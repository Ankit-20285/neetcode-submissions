class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_dict = {} 
        ans = []

        for s in strs: 
            x = sorted(s)
            a = "".join(x)
            if a not in my_dict: 
                my_dict[a] = [s]
            else: 
                my_dict[a].append(s)
        
        for keys, values in my_dict.items(): 
            ans.append(values)
        
        return ans