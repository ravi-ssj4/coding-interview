class Solution:
    '''
    method: intervals

    problem scoping:
        * clear that if any of the intervals overlap, he cannot attend all meetings
        * need to check if any of the intervals are overlapping!
        * how?
        
        * lightbulb moment: 
            - if startTime of current interval < end time of previous interval
                overlap exists between them, return false
            - need to sort according to start times
        * invariant : 
            * --- i1 --- i2 --- i3 --- 
            * if i2 is not overlapping with i1 (i2.start >= i1.end), then i3 will surely not
                overlap with i1 (i3.start > i2.start)
        
    algo:
        1. sort the intervals based on 0th(ie. start) index
        2. run loop from second interval till the end
            2.1. if prev interval's end value > current intervals's start value
                overlap exists -> return False
        3. return True

    time: O(nlogn) + O(n) = O(nlogn)
    space: O(1)
    '''
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0])

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True
