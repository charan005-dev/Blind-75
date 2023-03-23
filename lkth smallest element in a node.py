#TC: O(n) 
#SC: O(h)


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = 0
        self.k = k
        self.inorder(root)
        return self.result

    def inorder(self, root): #inorder traversal through recursion
        if not root or self.k <= 0: #stopping the recursion when the result is found
            return

        self.inorder(root.left)
        self.k-=1 #every time you encvounter a smaller element until k is 0, reduce k
        if self.k == 0:
            self.result = root.val #when k is 0, then the current value of root is our answer
        self.inorder(root.right)
            