from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

    # edge case: []
    if head is None:
        return head

    node = head
    while(node is not None):

        # if the current node is the last one, finish
        if node.next is None:
            break

        # if the next node has the same value as the current one
        # exclude the next node from the list
        if node.val == node.next.val:
            node.next = node.next.next
        
        # otherwise, move to the next node
        else:
            node = node.next

    return head

    


    