class Solution:
    '''
    method: sliding window
    algo:
        1. initialize two pointers l = 0 and r = 1 (l = day of buying stock, r = day of selling stock)
        2. if stock price on day r < stock price on day l, then update l = r
        3. else calculate profit by subtracting stock price on day r with stock price on day l
        4. update maxProfit at each step

    time: O(n)
    space: O(1)

    '''
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit
