class Solution:

    def maxDepth(self, root):
        return self.Depth(root,0)

    def Depth(self,root,counter):
        if not root:
            return counter
        elif self.Depth(root.right,counter+1) > self.Depth(root.left,counter+1):
            return self.Depth(root.right,counter+1)
        else:
            return self.Depth(root.left,counter+1)

