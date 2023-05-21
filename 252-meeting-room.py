class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the intervals by their start time in ascending order
        intervals.sort(key=lambda x: x[0])

        # Iterate through the intervals and check if there is any overlap between adjacent intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        # If there is no overlap between adjacent intervals, all meetings can be attended
        return True

    def isMeetingRoom(self, intervals):
        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0]
        for interval in intervals[1:]:
            next_start, next_end = interval

            if start <= next_end and next_start <= end:
                return False

            start = next_start
            end = max(end, next_end)

        return True
