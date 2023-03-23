#TC: O(n) 
#SC: O(h)



class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: 

        self.global_min = 1000 #set the global minimum which will be reduced while increasing the height
        if not root: 
            return [] 

        self.dfs(root,1)   #do inorder traversal by sending in the root and the counter
        return self.global_min    


    def dfs(self, root,c): 

        
        #base case 
        if root == None:        
            if c<self.global_min:   #whenever the count is lesser than global minimum, update it
                self.global_min = c 

        if root:
            self.dfs(root.left,c)   
        
        c+=1  #increase the counter during every recursion

        if root: 
            self.dfs(root.right,c)  
            