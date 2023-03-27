
#TC: O(m+n) M = nodes in P, N = nodes in Q 
#SC: O(h). height of the biggest tree(P or Q)

class Solution(object):
    def isSameTree(self, root, subRoot):
        
        if not root and not subRoot:
            return True
        

        #recursively check every node of both the trees whether they are in the same position
        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right))

        return False
    