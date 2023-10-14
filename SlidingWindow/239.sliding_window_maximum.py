class Solution:
    '''
    method: sliding window + deque
    algo:
        1. initialize output and l = r = 0 (we start with a window size of 1)
        2. initialize a deque (will store indices and not actual values from nums)
        3. iterate over nums using r
            3.1 while q is not empty and elements on top of queue are less than the current element
                keep on popping and then finally append the current element
            3.2 if the leftmost element of the queue is out of the window, remove it from the left
            3.3 if window is large enough 
                append the leftmost element in the queue into output
                increment l
            3.4 increment r
        4. return output
    
    time: O(n) 
    space: O(n)
    
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0
        q = collections.deque()

        while r < len(nums):
            # while there are smaller nums compared to our current element in the queue, 
            # keep on popping from right, then finally append the current element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
        
            # if the window has moved forward from what's there on the left of the queue
            # need to pop that
            if l > q[0]:
                q.popleft()
            
            # append into output array once the window becomes large enough:
            # also the left end of the queue starts moving from this point onwards only!
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output


