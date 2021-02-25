'''
in this we have to find if the tree is a  mirror image of itself, so we checked the children right 
left in outpair and inpair ie left's left and right's right and much more and then recursively return
the result. this was a nice question
'''



def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left,root.right)
        
def isMirror(self,left,right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    
    if left.val == right.val:
        outpair = self.isMirror(left.left,right.right)
        inpair = self.isMirror(left.right,right.left)
        return outpair and inpair
    else:
        return False