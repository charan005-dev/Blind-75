#TC: log(n) 
#SC: O(h)



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """ 

        #reduce the problem as binary search, go on the left if you have p and q less than the root, as the answer is going to be in the left 
        #else, go in the right side, there should be an answer, when p and q are smaller and greater than root at the same time, you are at the answer
        while root:
            if p.val<root.val and q.val<root.val:
                root = root.left

            elif p.val>root.val and q.val>root.val:
                root = root.right

            else:
                return root