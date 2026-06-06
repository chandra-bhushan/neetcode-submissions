# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = {}
        next = head.next        
        while next:
            if next in seen:
                return True

            seen[next] = True
            next = next.next

        return False

            
        