from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # Stores indices
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Record the maximum once the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        
        