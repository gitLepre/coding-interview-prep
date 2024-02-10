class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
    
    # recursion
    up = 0
    sum = l1.val + l2.val
    if (sum >= 10):
        sum %= 10
        up = 1
        
    # final state
    if (l1.next == None) and (l2.next == None):
        if(up):
            return ListNode(sum, ListNode(up)) # special case    
        return ListNode(sum)
    
    if (l1.next == None):
        l1.next = ListNode()
    
    if (l2.next == None):
        l2.next = ListNode()
    
    # add one to the next node if >= 10
    if(up):
        l1.next.val +=1 
    return ListNode(sum, self.addTwoNumbers(l1.next, l2.next))