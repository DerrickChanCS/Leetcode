"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        """
        This solution completes in O(n) time and O(n) space
        This solution works by creating a list from the nodes and removes the nth node
        """
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next
        if n == 1:
            if len(arr) == 1:
                return None
            arr[len(arr)-2].next = None
            return arr[0]
        if len(arr) == n:
            return arr[1]
        
        arr[len(arr)-n-1].next = arr[len(arr)-n+1]
        
        
        return arr[0]
