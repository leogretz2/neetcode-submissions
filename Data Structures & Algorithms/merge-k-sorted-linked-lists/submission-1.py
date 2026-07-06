# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # naive - take min of each and advance
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = {}
        dummyNode = ListNode()
        ret = dummyNode

        # initialize ptrs at start of each list
        for i, list_node in enumerate(lists):
            current[f"list{i}"] = list_node

        print('c',current)
        while current:
            minList = self.minOfNodes(current)
            # print('ml',minList)
            ret.next = current[minList]
            if current[minList].next:
                current[minList] = current[minList].next
            else:
                del current[minList]
            ret = ret.next

        return dummyNode.next

    def minOfNodes(self, node_lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_node = ListNode()
        minimum = float("inf")

        for node_list in node_lists:
            # print(node_list, node_lists[node_list].val)
            if node_lists[node_list].val < minimum:
                min_node = node_list
                minimum = node_lists[node_list].val
        
        return min_node