class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        for left in range(len(heights)): 
            for right in range(left + 1, len(heights)): 
                width = abs(left - right) 
                curr = min(heights[left], heights[right])
                area = width * curr 
                max_area = max(max_area, area)
            
        return max_area
        