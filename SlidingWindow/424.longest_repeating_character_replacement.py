class Solution:
    # '''
    # method 1: sliding window + dict of count of frequencies of chars so far
    # algo:
    #     1. initialize a count dict
    #     2. initialize 2 pointers l = r = 0 (sliding window = r - l  + 1)
    #     3. keep on moving pointer r(expanding the window) to the right until:
    #         * windowSize - count(maxFreqChar)(O(26)) <= k
    #             also update the longest substring length along
    #         * if its not so,
    #             * keep on decreasing window size and 
    #               decrementing the count of that char in the count dict

    #     4. return the longest substring len
    
    # time: O(n.26)
    # space: O(26)

    # '''
    # def characterReplacement(self, s: str, k: int) -> int:
    #     count = {}
    #     longest = 0
    #     l = 0
    #     for r in range(len(s)):
    #         # updating the count dict
    #         count[s[r]] = 1 + count.get(s[r], 0)
    #         # keep on decrementing the size of the window until 
    #         # winSize - countMaxFreqChar in count <= k
    #         while (r - l + 1) - max(count.values()) > k:
    #             count[s[l]] -= 1
    #             l += 1
    #         longest = max(longest, r - l + 1)

    #     return longest

    '''
    method 2:   * same as above with just 1 change -> no need to find maxOccuring char everytime from the dict
                * Reason:
                    * we will just store the occurance of maxFreq char seen so far in a variable
                    * the longest value only increases when the maxFreq value will increase,
                        ie. we see a char that incrases the freq of maxFreq var that's already in the window
                       -> otherwise, it does not matter if freq of some previous chars decrease
                * eg:
                    ->  windowSize = 6
                        maxFreq = 4, k = 2
                        so window is valid -> longest = 6
                        even if window shrinks, it won't update the longest var
                        longest var is only updated if maxFreq becomes more
                        Eg: winSize = 7, maxFreq = 5, then longest = 7
    time: O(n)
    space: O(26)
    '''

    def characterReplacement(self, s, k):
        longest = 0
        count = {}
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest