class Solution:
    '''
    method 1: sliding window + 2 hashMaps + window minimization from the left
                ie. keep on minimizing window from the left until our condition
                holds(have == need), else try increasing the window from the right
                so that we find a char so that our condition(have == need) becomes true again
    
    algo:
        1. initialize the two hashMaps countT and window
        2. fill the value of countT hashMap as its going to be fixed throughout
        3. iterate over s in a sliding window fashion
            a. r focuses on increasing the window size and l focuses on shrinking / minimizing the window
            b. initially l = 0, r = 0 and win size = 1
            c. keep on increasing the window and checking if have == need condition is satisfied
            d. if loop,
                1. keep on shrinking the window(removing the char from window hashMap and comparing) 
                   and checking if have == need is still holding
                2. then adding the current window [l, r] and current window size = r - l + 1 to the result
                 
    time: O(n)
    space: O(26)
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        
        countT, window = {}, {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # initialize have and need
        have, need = 0, len(countT) # countT's len gives unique chars in t only

        res, resLen = [-1, -1], float("inf")
        
        l = 0
        for r in range(len(s)):
            # add the current char to the window dict
            window[s[r]] = 1 + window.get(s[r], 0)

            # if this char is in countT 
            # and also adding it to the window made the count of 
            # this char in both hashMaps equal for the first time, 
            # then increase the have variable value
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                # add to the result
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                # start trying to minimize the window from the left
                window[s[l]] -= 1
                # if this char is in countT 
                # and also removing it from the window made the count of 
                # this char in both hashMaps unequal for the first time, 
                # then decrease the have variable value
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""