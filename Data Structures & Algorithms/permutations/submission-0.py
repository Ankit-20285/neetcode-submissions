class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():

            # Base case
            if len(current) == len(nums):
                result.append(current[:])
                return

            # Try every unused number
            for i in range(len(nums)):

                if used[i]:
                    continue

                # Choose
                current.append(nums[i])
                used[i] = True

                # Explore
                backtrack()

                # Undo (Backtrack)
                current.pop()
                used[i] = False

        backtrack()

        return result