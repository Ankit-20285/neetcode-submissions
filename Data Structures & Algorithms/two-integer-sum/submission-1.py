class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)): 
            needed = target - nums[i]

            if needed in my_dict: 
                return [my_dict[needed], i]
            
            my_dict[nums[i]] = i
        