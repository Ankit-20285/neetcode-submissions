class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = {}

        for num in nums:
            if num in my_dict:
                return num
            my_dict[num] = 1
