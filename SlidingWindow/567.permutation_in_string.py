class Solution:
    '''
    method 1: sliding window + sorting of possible anagrams for each window -> O(n * m)
    
    method 2: sliding window + 2 hashmaps (1 overall and 1 per window) -> O(26.n)
    algo:
        1. start with a window of size of s1 (bounded by l and r)
        2. create 2 hashMaps
            1. Overall hashmap for entirety of s2
            2. hashMap for s1
        2. Iterate over s2 from len(s1) till s2
            * at each iteration do a comparision of the hashMaps (ie. the overall Hashmap and the window hashmap)
            * if equal, return true
            * else,
                update the window and the hashMap accordingly and continue with next iteration
    
    time: O(26.n)
    space: O(26)

    method 3: sliding window + 2 fixed hashMaps but more efficient -> O(n)
    logic:
        * only difference from method 2:
            1. no need to do a O(26) comparision at every iteration
            2. keep a variable "matches" that's updated at each window
                * if matches == 26, return True
                * else continue iterating and updating hashMaps and "matches"
    
    time: O(n)
    space: O(26)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case:
        if len(s1) > len(s2): return False 
        # initialize 2 hashMaps/count arrays to 0s
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # update the first and second hashmaps/count ararys till the length of s1 === length of first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # update the matches variable after scanning through the 2 hashMaps once
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
    
        # iterate over s2 in terms of windows and check for matches == 26 
        l = 0
        # keep on adding char at r and removing char at l
        for r in range(len(s1), len(s2)): 
            if matches == 26:
                return True
            
            # for the addition of new char to the window
            indexR = ord(s2[r]) - ord('a')
            s2Count[indexR] += 1
            # in case addition caused increase in num of matches
            if s1Count[indexR] == s2Count[indexR]:
                matches += 1
            elif s1Count[indexR] + 1 == s2Count[indexR]:
                # in case addition caused decrease in num of matches (means earlier they were matching)
                matches -= 1

            # for the deletion of old char from the window
            indexL = ord(s2[l]) - ord('a')
            s2Count[indexL] -= 1
            # in case removal caused increase in num of matches
            if s1Count[indexL] == s2Count[indexL]:
                matches += 1
            elif s1Count[indexL] - 1 == s2Count[indexL]:
                # in case removal caused decrease in num of matches (means earlier they were matching)
                matches -= 1
            # need to increment l as well
            l += 1
        # in case matches == 26 was not checked before the loop terminated
        return matches == 26