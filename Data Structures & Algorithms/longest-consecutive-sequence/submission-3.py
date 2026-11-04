class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        count = 1

        nums.sort()

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] - nums[i-1] == 1:
                count += 1

            elif nums[i] == nums[i-1]:
                continue

            else:
                ans = max(ans, count)
                count = 1

            ans = max(ans, count)

        return ans