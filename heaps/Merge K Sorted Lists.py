# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        node_heap = []

        #Generate heap of nodes
        # 1  1  1  2  3
        #             c  n
        #   1 3 4
        #    
        for linked_list in lists:

            curr = linked_list
            next = None 

            while curr:
                next = curr.next
                curr.next = None
                heap_element = (curr.val, len(node_heap), curr)
                # print(curr.val)
                # print(heap_element)
                # print(type(heap_element))
                heapq.heappush(node_heap, heap_element)
                curr = next 

        #While heap, pop node off and link it to final linked list        
        head = None
        if node_heap:
            val, heap_len, node = heapq.heappop(node_heap)
            head = node
            curr = head 
        
        while node_heap:
            val, heap_len, node = heapq.heappop(node_heap)
            curr.next = node 
            curr = curr.next 
        
        return head 

