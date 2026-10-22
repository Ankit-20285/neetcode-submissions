class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = n - 1

            while L < R:
                total = nums[i] + nums[L] + nums[R]

                if total == 0:
                    res.append([nums[i], nums[L], nums[R]])

                    while L < R and nums[L] == nums[L + 1]:
                        L += 1

                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1

                    L += 1
                    R -= 1

                elif total > 0:
                    R -= 1

                else:
                    L += 1

        return res