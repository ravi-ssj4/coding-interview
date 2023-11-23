class Solution:
    '''
    method: greedy about difference[i] = (gas[i] - cost[i])
    algo:
        1. if sum of gas < sum of cost, can't complete the cyclic journey
        2. run a loop = len of the gas/cost array
            at each iteration, calculate the diff (total = gas[i] - cost[i])
            if total < 0:
                restart the journey from next position (start = i + 1)    
        3. return starting point of the journey from where we could travel a cycle of distance
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1
            
        return start