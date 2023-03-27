#TC: O(n) 
#SC: O(h)
class Solution(object): 
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.res=[]
        self.target = targetSum
        self.dfs(root,0,[])
        return self.res
        
    def dfs(self,root,currsum,path):
        #print(path,currsum)
        if root==None:
            return
           
        
        #action        
        path.append(root.val)
        currsum = currsum+root.val  #add the root val to the currsum until it equals the target
                
        if root.right==None and root.left==None: #when recursion unfolds

            if currsum==self.target:
                self.res.append(path[:]) #if currsum equals the target, append it inside the result
         
        #recursion done on left subtrees and right subtrees
        self.dfs(root.left,currsum,path) 
        
        self.dfs(root.right,currsum,path)
        
        
        #backtrack by your own everytime you completed witnessing a path
        path.pop()