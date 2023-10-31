class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None


class LRUCache:
    '''
    method: hashMap(key: key, value: addr of node of LL) + linkedlist to keep track of (key,value) pairs
    problem scoping:
        1. need to access values in O(1) time -> hashMap
        2. need to keep track of order of values entered -> array or Linkedlist
            -> linkedlist is more suited since its address can 
                be stored as value for a particular key in the hashmap
            -> eg. (1,1) -> (2,2) -> None
        3. need to keep track and access LRU and MRU in O(1) -> doubly linked list instead of singly
        4. to keep track of lru and mru, need 2 additional pointers(dummy nodes in case of python
            -> left = (0, 0) and right = (0, 0)
        5. left(LRU) <-> (1,1) <-> (2,2) <-> right(MRU)
        6. get(1) ->
            remove(1,1) and insert to the right of (2,2) between (2,2) and right node
            left(LRU) <-> (2,2) <-> (1,1) <-> right(MRU)
        7. put(3,3) ->
            if key already exists, remove it, ie. delete the node!
            make new node and insert into hash table
            insert this new node into the linked list -> at MRU, ie. between prev node of right and right
            left(LRU) <-> (2,2) <-> (1,1) <-> (3,3) <-> right(MRU)
    
    algo:
        1. Create a new class Node for nodes of the doubly LinkedList
            (Note: the doubly linkedlist is always bounded by left and right nodes hence any node
            that is to be removed, the case is -> (Node1 <-> middle <-> Node3) -> delete middle!)
        1.1. create 2 helper functions remove and insert(inserts to the right of the doubly linked list
                            ie. between prev of MRU and MRU)

        2. Initialize the data structures
            0. initialize capacity
            a. hashMap -> cache
            b. left and right nodes of the doubly linked list and connect them properly

        3. Get operation:
            3.1. if key exists in the hashmap
                    a. first remove the corresponding node from the doubly linked list
                    b. then insert the node into the doubly linked list at mru position
                    c. then return the value

        4. Put operation
            4.1. if key already present in hashMap, remove it
            4.2. insert Node into the hashMap (key: node)
            4.3. insert the node into the doubly linked list
    '''
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: Node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove the node directly from the middle of two nodes
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert to the right of doubly linkedlist
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        if key in self.cache:
            # removal only breaks the links and does not actually
            # delete the node, so it can be inserted at a different position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 # in case key is not present

    def put(self, key: int, value: int) -> None:
        # if key is already present, remove the node
        if key in self.cache:
            self.remove(self.cache[key])
        # insert it into the cache and the linkedlist
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        # check if capacity overflowed!
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # that's why we saved keys again in the nodes of the linked list



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)