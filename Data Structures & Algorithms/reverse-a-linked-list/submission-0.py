# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# current = 0 > 1(current.next) > 0
# forwardNext = 1
# prev = 0

# current = 0 .next = None
# forwardNext = None > 1 (current.next)
# prev = None > 0



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            forwardNext = current.next # store forward list
            current.next = prev # point current node back
            prev = current # move previous node up
            print(prev.val)
            current = forwardNext # current becomes stored next node

        # current is now null, prev is last element
        return prev

