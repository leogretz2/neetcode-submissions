# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # merge two lists at a time
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None
        current = lists[0]
        for i in range(1, len(lists)):
            current = self.mergeTwoLists(current, lists[i])
        
        return current
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ret = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                ret.next = list1
                list1 = list1.next
            else:
                ret.next = list2
                list2 = list2.next
            ret = ret.next
        # append remaining
        ret.next = list1 if list1 else list2
        
        return dummy.next

        