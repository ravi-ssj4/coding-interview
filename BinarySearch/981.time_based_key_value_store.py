class TimeMap:

    def __init__(self):
        self.store = {} # key: list of [value, timestamps]

    # time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    # the main tricky function
    # time: O(logn)
    def get(self, key: str, timestamp: int) -> str:
        res = ""

        # get the list of lists pointed to by the key,
        # if not present, get an empty list
        array = self.store.get(key, [])

        l, r = 0, len(array) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if array[mid][1] <= timestamp:
                # make the current mid element as a potential answer
                # (in case exact timestamp is not present)
                # when we go searching in the right(this mid element will
                # be the answer in that case)
                res = array[mid][0]
                l = mid + 1
            else:
                # if middle element > timestamp, possible closer value has
                # to be in the left side 
                r = mid - 1
            
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)