class Solution:
    '''
    problem scoping:
        * intervals are not sorted -> need to sort them
        * can just iterate over intervals and keep on checking if current interval
            if overlaps with the previous one,
                merge current and prev and add to output 
            else directly add current to output
    algo:
        1. sort the intervals based on start time
        2. output = [intervals[0]] - to take care of edge case
        3. iterate from 2nd to the last interval
            3.1. if prev interval's end > current interval's start:
                merge and append to output
            3.2. directly append current interval to output
        4. return output
    
    Note: [1, 2] and [2, 3] will also overlap and need merging

    time: O(nlogn)
    space: O(1)
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output