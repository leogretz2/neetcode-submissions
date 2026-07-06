# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        lists = [l for l in lists if l] # drop empty

        while len(lists) > 1:
            merged = []
            # 0 necessary?
            for i in range(0,len(lists),2):
                if i+1 < len(lists):
                    merged.append(self.mergeTwoLists(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])
            lists = merged
        return lists[0]

        
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