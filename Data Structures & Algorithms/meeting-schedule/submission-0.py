"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by start time
        intervals.sort(key=lambda i: i.start)
        
        # Check adjacent intervals for overlaps
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            
            if curr.start < prev.end:
                return False
                
        return True