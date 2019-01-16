class Solution:
    def isSameTree(self, p, q):
        if p==None or q==None:
            return False
        elif p.val==q.val and p.left==None and p.right==None and q.left==None and q.right==None:
            return True
        elif self.isSameTree( p.right, q.right)==True and self.isSameTree(p.left, q.left)==True:
            return True
        else:
            return False
