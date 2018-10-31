# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            left_len = left+1 if root.left and root.left.val == root.val else 0
            right_len = right+1 if root.right and root.right.val == root.val else 0
            self.longest = max(self.longest, left_len + right_len)
            return max(left_len, right_len)
        traverse(root)
        return self.longest
