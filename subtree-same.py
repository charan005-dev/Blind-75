



class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot): 
            return True
        
        #if you find the subtree recursively on the left side or right side, then return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        

    def sameTree(self, root, subRoot): #same tree function
        if not root and not subRoot:
            return True
        
        #recursively check every node of both the trees whether they are in the same position
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))

        return False