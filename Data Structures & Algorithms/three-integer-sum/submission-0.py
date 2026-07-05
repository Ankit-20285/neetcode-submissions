class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                          # Step 1: Sort the array
        result = []

        for i in range(len(nums) - 2):      # Step 2: Fix pivot i
            if nums[i] > 0:
                break                        # Optimization: no triplet possible
            if i > 0 and nums[i] == nums[i - 1]:
                continue                     # Skip duplicate pivot

            L, R = i + 1, len(nums) - 1    # Step 3: Two pointers

            while L < R:
                s = nums[i] + nums[L] + nums[R]

                if s == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]: L += 1  # skip dup L
                    while L < R and nums[R] == nums[R - 1]: R -= 1  # skip dup R
                    L += 1
                    R -= 1
                elif s < 0:
                    L += 1                   # Sum too small, move L right
                else:
                    R -= 1                   # Sum too large, move R left

        return result