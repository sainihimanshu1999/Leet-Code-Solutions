def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)
    if(leftdepth > rightdepth):
        return leftdepth + 1
    else:
        return rightdepth + 1