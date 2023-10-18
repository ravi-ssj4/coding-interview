class Solution:
    '''
    problem scoping:
        * again, hint: example intervals are sorted 
            -> need to sort to find overlapping intervals
        * we need to draw the intervals out on paper to actually understand
          how to proceed at least in this problem!
        * lightbulb moment:
            * whenever there's an overlap, [1, 2], [1, 3], [2, 3]
             -> if we remove [1, 2], then again [1, 3] and [2, 3] will overlap and we again have to remove one more!
             -> if we remove [1, 3], then that's it, [1, 2] and [2, 3] are non-overlapping
             
            * lightbulb moment 2: so, whenever we have an overlap, remove the interval having greater end value!
    
    algo:
        1. sort the intervals array directly 
            (first it'll be sorted on start times and if there's a tie, it'll be sorted on end time)
        2. initialize removals = 0, prevEnd = intervals[0][1] (the end value of first interval)
        3. iterate from second interval onwards
            3.1. if start of current interval >= prevEnd
                * no overlap
                * just update the prevEnd = current interval's end 
                    (since end of current interval has to be > prevEnd)
            3.2. else
                * removals += 1
                * update the prevEnd = min(prevEnd, currentEnd) 
                    Remember that we are removing the interval that has greater end value, and hence
                    keeping the interval which has smaller end value!
        4. return removals
                 
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        removals = 0
        for start, end in intervals[1:]:
            if prevEnd <= start:
                # no overlap
                prevEnd = end
            else:
                removals += 1
                prevEnd = min(prevEnd, end)
        return removals













