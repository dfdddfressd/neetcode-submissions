"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                print(intervals[i].end)
                print(intervals[j].start)
                if not (intervals[i].end <= intervals[j].start) and not (intervals[i].start >= intervals[j].end):
                    return False
        return True

