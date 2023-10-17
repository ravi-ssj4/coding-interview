class Solution:
    '''
    * problem scoping: 
        * after drawing on paper
            * need to find max number of overlap at any given point of time
        * Stack ? -> no fails because everytime, for current interval, we need to check if its overlapping
                    with any of the previous intervals(cannot just look at the last interval)
                -> also, even if looking at all previous intervals is possible,
                    -> need to look at the prev interval with least end time, so that comparing with that one,
                        if current interval dosen't overlap, then number of meeting rooms required can be decreased by 1
        * lightbulb moment -> sort the end times and store separately
    
    * algo:
        1. create two arrays start and and with start and end times of the interval in sorted order
        2. iterate over the two arrays simultaneously
            2.1. if current start value < current end value:
                    -> overlalp exists:
                        need one more meeting room
                * count += 1
                * s += 1 ( move on to the next meeting's start value)
            2.2. else:
                    -> no overlap with the current end value meeting
                * count -= 1
                * e += 1 (move on to the next meeting's end value)

                
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        res, meetings = 0, 0

        # if start array is exhausted, no need to further
        # iterate because iterating over end array only
        # decrements the counter
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                meetings += 1
                s += 1
            else:
                meetings -= 1
                e += 1
            res = max(res, meetings)
        return res














