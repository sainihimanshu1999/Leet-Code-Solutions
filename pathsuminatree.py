'''
method one to solve
it is same as second one but more conscise solution and easier to understand
'''


def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)



'''
Method 2 to solve this, more elaborate approach
this will explain the above mehtod fully.
'''


def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return(targetSum == 0)
        else:
            ans = 0
            sbsum = targetSum - root.val
            
            if(sbsum ==0 and root.left is None and root.right is None):
                return True
            
            if root.left is not None:
                ans = ans or self.hasPathSum(root.left,sbsum)
            if root.right is not None:
                ans = ans or self.hasPathSum(root.right,sbsum)
            
            return ans
        