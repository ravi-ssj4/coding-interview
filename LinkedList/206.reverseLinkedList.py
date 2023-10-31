# 1 -> 2 -> 3 -> 4 -> 5 => 5 -> 4 -> 3 -> 2 -> 1

#                     p    c    n
# 1 <- 2 <- 3 <- 4 <- 5 

class ListNode:
	def __init__(self, value):
		self.value = value
		self.next = None

def  reverseList(head: [ListNode]):
	
	prev = None
	cur = head
	
	while cur:
		next = cur
		cur.next = prev
		prev = cur
		cur = next
	
	return prev