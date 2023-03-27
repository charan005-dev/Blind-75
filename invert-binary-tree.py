#TC:O(n) 
#SC:O(h)
#BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 

        if not root:
            return root
        q=deque()
        q.append(root)        
        while q:
            node = q.popleft() 
            #swap left and right nodes
            node.left , node.right = node.right , node.left            
            #left check
            if node.left:
                q.append(node.left)
            #right check
            if node.right:
                q.append(node.right)
        return(root)  

#TC:O(n) 
#SC:O(h)
#DFS 

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.postorder(root)
        return root

    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        root.left,root.right = root.right,root.left #postorder traversal

