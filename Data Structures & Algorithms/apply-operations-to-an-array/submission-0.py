class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        L = 0

        for R in range(n):
            if nums[R] != 0:
                nums[L] = nums[R]
                L += 1

        while L < n:
            nums[L] = 0
            L += 1

        return nums