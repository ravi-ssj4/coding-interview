class Solution:
    '''
    method: intervals

    problem scoping:
        * intervals are already sorted!
        * lightbulb moment:
            * simply traverse over all the intervals 
                * case 1: insert the new interval at its correct position if no overlap exists
                * case 2: keep on merging with overlapping intervals(can be multiple)
            *         s---e         s---e s---e s---e
            *           i1            i2    i3    i4
            * s-new-e                                    -> no overlap -> directly insert new interval
            *               s-new-e                      -> no overlap -> insert current interval i2 and keep on testing with the future ones
            *            s-new-e                         -> overlap -> merge -> new interval = [min(starts), max(ends)]

    algo:
        1. initialize res
        2. iterate over all intervals left to right(already sorted)
            2.1. if newInterval's end < currentInterval's start
                    no overlap of newInterval with any intervals ahead of it!
                    res.append(newInterval) + rest of the intervals
            2.2. elif currentInterval's end > new Interval's start
                    no overlap of current interval with the new interval and it can be safely added
                    res.append(currInterval)
            2.3. else
                    overlap exists between current and new interval, 
                    update new interval but do not push anything because the updated new interval might overlap with
                    upcoming intervals
                    update new interval = [min(start values), max(end values)]
            2.4. add newInterval in case it was the last interval and was updated
            2.5. return res

        Note: one major edge case:
                i1 : [0, 1]
                i2 : [1, 2]
                these will also overlap and merge!
    
    time: O(n)
    space: O(1)

    dry run:
    
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else: 
                # overlap between the current and the new interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # in case the newInterval got updated and it was the last interval, need to add it as well
        res.append(newInterval)
        return res

