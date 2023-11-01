# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    method: set GroupPrev and groupNext pointers and reverse the inbetween nodes and reconnect
            pointers correctly
    
    problem scoping:
        dummy --> 1 --> 2 --> 3 --> 4 --> 5 --> Null
        grpPrv              grpNxt

        * grpPrv = dummy 
        while True:
            * kth = getKth()
            * if not kth:
                break
            * grpNxt = kth.next
            * reverse(kth till grpNext)
                * prev.next = grpNxt
                * cur = grpPrev.next
                * while cur != grpNxt:
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                * tmp = grpPrev.next
                * connect prev group to head of current reversed group
                    * grpPrev.next = kth
                * grpPrev = tmp
    
    time: O(n)
    space: O(1)
    '''
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse until groupNext
            cur = groupPrev.next
            prev = groupNext
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp2 = groupPrev.next
            # to connect to the head of next group which was just reversed
            groupPrev.next = kth
            # to put groupPrev to the prev node of the next group to be reversed
            groupPrev = tmp2
        return dummy.next

    
    def getKth(self, cur, k):
        while k > 0:
            cur = cur.next
            k -= 1
        return cur