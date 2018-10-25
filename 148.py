"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        1) get middle of linked list O(n)
        2) sort the lists
        2) merge two linked lists O(n)
        """
        if head is None or head.next is None:
            return head
        
        l2 = head
        temp = head
        # 1) get the middle of the linked list
        while temp and temp.next:
            prev = l2
            temp = temp.next.next
            l2 = l2.next
        
        prev.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(l2)
        
        return self.mergeList(l1, l2)
    
    def mergeList(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        head = ListNode(0)
        temp = head
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return head.next
        
