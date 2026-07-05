# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # fast/slow technique
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        current = head
        currentFast = head
        while current.next and currentFast.next:
            current = current.next
            if not current:
                return False
            currentFast = currentFast.next
            # not necessary
            # if currentFast:
            currentFast = currentFast.next
            if not current or not currentFast:
                return False
            if current == currentFast:
                return True
        return False
