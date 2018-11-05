"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        queue = deque()
        queue.append((root, 0))
        curLevel = 0
        ans = []
        while queue:
            temp = deque()
            curLevel = queue[0][1]
            while queue and queue[0][1] == curLevel:
                node, level = queue.popleft()
                if not node: continue
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                
                if curLevel % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
            if temp:
                ans.append(list(temp))
        return ans
