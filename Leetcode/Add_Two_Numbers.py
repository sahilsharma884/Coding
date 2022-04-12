# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        prev = None
        temp = None
        carry = 0
        while (l1 is not None or l2 is not None):
            fdigit = 0 if l1 is None else l1.val
            sdigit = 0 if l2 is None else l2.val
            sumdigit = carry + fdigit + sdigit
            
            carry = 1 if sumdigit > 9 else 0
            
            sumdigit = sumdigit if sumdigit < 10 else sumdigit % 10
            
            temp = ListNode(sumdigit)
            
            if head is None:
                head = temp
            else:
                prev.next = temp
                
            prev = temp
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry > 0:
            temp.next = ListNode(carry)
            
        return head