def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return self.minDepth(root.right)+1
    if root.right is None:
        return self.minDepth(root.left)+1
    return min(self.minDepth(root.left),self.minDepth(root.right))+1
        