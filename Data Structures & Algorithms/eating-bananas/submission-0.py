from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        while left <= right: 
            count = 0
            mid = (left + right)//2 
            for pile in piles: 
                count += ceil(pile/mid)
            
            if count <= h: 
                right = mid - 1
            else:
                left = mid + 1

        return left
    
