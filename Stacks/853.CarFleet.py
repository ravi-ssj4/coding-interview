class Solution:

    '''
    scoping the problem:
        n cars -> direction l to r
        one lane road
        positions and speeds given
        distance of each car from target = target - position
        time taken for that = distance / speed
    
        lightbulb moment:
            * ----- car1 ----- car2 ----- target
                if time taken by car1 <= time taken by car2,
                    car1 will catch up to car2 and both will become a fleet
            
            * --- car1 --- car2 --- car3 --- car4 ------ target
                if we traverse from left to right, and try to figure out if car1 and car2 join at some point,
                    car2's speed cannot be certain because it can join car3 before joining with car1 and start
                    travelling with the speed of car3
                hence, we traverse from right to left!
            
            * if car3 dosen't join car4, certainly car2 cannot join car4 because it'll hit car3 before car4 and
                get limited by the speed of car3 and car3 itself dosen't have enough speed to join car4!
        
    algo:
        1. initialize an empty stack
        2. initialize a list of pairs of [position,speed]
        3. sort this list of pairs according to positions
            Note: each pair in this list represents a car
        4. iterate over the list of pairs from right to left
            4.1. push the time required by the current car onto the stack
            4.2. once length of stack becomes >= 2
                look onto the top and second top elements of the stack
                if top <= second top, means this car will catch up to the car ahead of it
                    remove this car's existance by popping it out of the stack
        8. return len(stack)

    dry run:
    position = [10,2,5,7,4,6,11]
    speed = [7,5,10,5,9,4,1]
    pair = [[11, 1], [10, 7], [7, 5], ..]
    stack = [[11, 1]]
    within loop:
        p = 10
        s = 7
        currentCarTime = 1.4
        stackP = 11
        stackS = 1
        stackCarTime = 11

    '''

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p, s in zip(position, speed)]

        # pair = sorted(pair)
        # stack = [pair[-1]]
        # for i in range(len(pair) - 2, -1, -1):
        #     p, s = pair[i]
        #     print(p, s)
        #     currentCarTime = (target - p) / s
        #     stackP, stackS = stack[-1]
        #     stackCarTime = (target - stackP) / stackS
        #     if currentCarTime <= stackCarTime: # collision will occur
        #         stack.pop()
        #         stack.append([stackP, stackS])
        #     else:
        #         stack.append([p, s])

        # optimized code
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # latest car will join the car ahead of it and hence, its existance is overshadowed
        return len(stack)
