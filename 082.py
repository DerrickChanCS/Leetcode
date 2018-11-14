"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def killDupes(head):
            if not head:
                return
            ptr = head
            if ptr.next and ptr.val == ptr.next.val:
                while ptr.next and ptr.val == ptr.next.val:
                    ptr = ptr.next
                return killDupes(ptr.next)
            else:
                ptr.next = killDupes(ptr.next)
            return ptr
        
        return killDupes(head)
        """
        dummy = ListNode(0)
        dummy.next = head
        prevUnique = dummy
        prev = None
        ptr = head
        while ptr:
            while ptr.next and ptr.val == ptr.next.val:
                ptr = ptr.next
            prevUnique.next = ptr.next
            if ptr.next and ptr.val != ptr.next.val:
                prevUnique = ptr
            ptr = ptr.next
        """
                
