class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums: 
            if i not in my_dict: 
                my_dict[i] = 1
            else: 
                my_dict[i] += 1

        sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)
        return sorted_keys[:k]