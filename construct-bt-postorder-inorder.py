#TC: O(n) 
#SC: O(n)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        
        #everytime, we have to search the root in preorder and set it as pivot
        for i in range(len(inorder)): 
            if inorder[i] == preorder[0]:
                pivot = i
        
        #perform recursion for each node on left and right to have new preorder and inorder arrays and build based on the current values
        root.left = self.buildTree(preorder[1:pivot+1],inorder[:pivot]) 
        root.right = self.buildTree(preorder[pivot+1:],inorder[pivot+1:])

        return root