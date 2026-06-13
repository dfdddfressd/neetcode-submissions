# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        checked = []
        

        while curr:
            temp = curr.next
            if temp not in checked:
                checked.append(curr)
                curr = curr.next
            else:
                return True
            
        
        return False
        