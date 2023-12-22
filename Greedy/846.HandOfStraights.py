class Solution:
    '''
    method: greedy + hashMap + minHeap (take the min value everytime as a probably start of group of size = groupSize)
    algo:
        1. if hand is not divisible by groupSize, 
            then return False
        2. update the hashMap with frequencies of values in the hand 'count'
        3. create a minHeap 'minH' using the keys of the hashmap 
        4. while minHeap is not empty
            4.1. first = extract-min() from minHeap
            4.2. try for a sequence of values 'i' from (first) till (first + groupSize)
                1. if i not in hashmap:
                    return False
                1. decrement count[i]
                3. if count[i] == 0
                    3.1. if i != extract-min() in minH:
                        return False
                    3.2. pop from minHeap
        5. return True (if we did not return false at points 1, 4.2.1. and 4.2.3.2 return True)
    
    time: O(nlogn)
                                
    '''
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        minH = list(count.keys()) # count.keys() is immutable set, we need to mutate, hence convert to list
        heapq.heapify(minH) # O(n) algo to create minHeap out of a list

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH) # O(logn) algo to pop min element and then heapify to restore min heap property
        return True