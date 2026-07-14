class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        return expected_sum - sum(nums)
        