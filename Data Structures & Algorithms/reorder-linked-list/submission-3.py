# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        dummyHead = ListNode()
        ret = dummyHead
        secondHalf = self.findMiddle(head)
        reversedStart = self.reverseList(secondHalf)
        # print('dsff',head.val,reversedStart.val)
        ret = self.mergeLists(head,reversedStart)

    def findMiddle(self, head: Optional[ListNode]) -> None:
        slowPtr = head
        fastPtr = head
        while fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
            if fastPtr.next:
                fastPtr = fastPtr.next
        
        # slowPtr = slowPtr.next
        # fastPtr = fastPtr.next
        print(slowPtr.val, fastPtr.val)
        return slowPtr

    def reverseList(self, head: Optional[ListNode]) -> None:
        current = head
        prev = None

        while current:
            # temp = current
            next_node = current.next # store forward list
            current.next = prev # set previous node to current's next (flip direction)
            prev = current # move prev forward
            current = next_node # move current forward

        # current will be None (loop condition)
        return prev

    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> None:
        print('bal0',not list1, list1, list1.val, list2, list2.val)
        if not list1:
            return list2
        ret = list1
        list1Input = 0
        list1 = list1.next
        # list1Input = not list1Input
        # while list1.next and list2.next:
        print('bal',not list1, list1, list2)#, list1.val, list2.val)
        # list1 does not end
        while list1 != list2: # and (list1.next and list2.next):
            # print('dsf',list1.next.val,list2.next.val, ret.val, list1Input)
            if list1Input:
                ret.next = list1
                list1 = list1.next
                list1Input = not list1Input
            else:
                ret.next = list2
                list2 = list2.next
                list1Input = not list1Input
            ret = ret.next
            print('end',ret.val, f"{list1.val}:", list1, f"{list2.val}:", list2, list1Input)
        print('aft',list1.val, list2.val)

        ret = list1 if list1 else list2

        return ret
