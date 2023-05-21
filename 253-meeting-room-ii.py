import heapq
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort the intervals by their start time in ascending order
        intervals.sort(key=lambda x: x[0])

        # Initialize a heap to keep track of the end time of meetings
        # that are currently in progress
        heap = []

        # Iterate through the intervals and check if each meeting can be assigned to a room
        for interval in intervals:
            # If the heap is empty or the end time of the earliest meeting in the heap is
            # earlier than the start time of the current meeting, assign a new room for the
            # current meeting
            if not heap or heap[0] > interval[0]:
                heapq.heappush(heap, interval[1])
            # If the end time of the earliest meeting in the heap is later than or equal to
            # the start time of the current meeting, find an available room to use or create
            # a new one
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval[1])

        # The length of the heap represents the minimum number of meeting rooms needed
        return len(heap)

    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        # Extract the start times and end times of all meetings into separate lists
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])

        # Initialize variables to keep track of the number of meeting rooms needed and
        # the number of ongoing meetings
        num_rooms_needed = 0
        num_ongoing_meetings = 0

        # Iterate through the start times and end times of all meetings
        i = 0
        j = 0
        while i < len(start_times) and j < len(end_times):
            # If the current meeting has already ended, increment the number of
            # ongoing meetings and move to the next end time
            if end_times[j] <= start_times[i]:
                num_ongoing_meetings -= 1
                j += 1
            # If there is an available meeting room, schedule the current meeting
            # and increment the number
            # of ongoing meetings and the number of meeting rooms needed
            else:
                num_ongoing_meetings += 1
                num_rooms_needed = max(num_rooms_needed, num_ongoing_meetings)
                i += 1

        # The final result is the number of meeting rooms needed
        return num_rooms_needed

    def minMeetingRooms2(self, intervals):
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        meeting_rooms = 0
        ongoing_meetings = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            meeting_rooms = max(meeting_rooms, ongoing_meetings)

        return meeting_rooms
