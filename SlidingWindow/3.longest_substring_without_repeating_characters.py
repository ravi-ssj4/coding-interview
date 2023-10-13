class Solution:
    '''
    method: sliding window + hashSet per window
    algo:
        1. initialize two pointers l and r to point to first element
        2. keep on trying to expand the window size by moving r one step ahead in each iteration
        3. if r comes to an element already in the window(figure out via the hashSet)
        4. keep on removing the elements from the left side of the window until this element is still
            in the hashSet, also keep on removing those elements from the hashSet
            ie. hashSet must be sync with the current window

    example:
        a b c a b c b b
        l     r
        hashSet = [a, b, c]

    time: (n)
    space: O(n) hashSet in worst case has to contain all elements(if all elements are distinct)

    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashSet = set()
        longest = 0
        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest