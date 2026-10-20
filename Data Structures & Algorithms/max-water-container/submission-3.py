class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 
        R = len(heights) - 1 
        Length = float('inf')
        Area = float('-inf')
        
        while L <= R: 
            Width = R - L 
            Length = min(heights[L], heights[R])
            Area = max(Area, Width * Length)

            if heights[R] > heights[L]: 
                L += 1 
            else: 
                R -= 1 

        return Area
