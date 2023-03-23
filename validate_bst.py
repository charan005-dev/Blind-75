#TC: O(n) 
#SC: O(h) - height of the tree


#recursion unfolds when the recursion hits the none node 
#call in the order of left, root and right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.li = []
        self.prev = float("-inf")
        self.flag = True
        self.inorder(root)
               
        return self.flag

    def inorder(self,root):
        if root==None or not self.flag:
            return

        self.inorder(root.left)
        
        if root.val<=self.prev:
            self.flag = False
        self.prev = root.val

        self.inorder(root.right)