# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        elif root.val==sum and root.left==None and root.right==None:
            return True
        else:
            sum-=root.val
            return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

