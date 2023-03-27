#BFS
#TC: O(n)
#SC: O(h) - height of the tree is 'h'
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:  #if root is not present, then return an empty list
            return []
        result=[] #open a resultant list
        q=deque() #q will be our queue
        q.append(root) #initially root goes inside q
        
        while q: #traverse through the q
            size = len(q) #size of q is important to traverse through the entire level
            level=[]
            for i in range(size): #traverse through the level
                node = q.popleft() #node will be first ele in q
                level.append(node.val) #append it to val
                #left check
                if node.left:
                    q.append(node.left) #append the left child to q
                #right check
                if node.right:
                    q.append(node.right) #append the right child to q

            result.append(level[-1]) #now, last element of level gets appended in result
        return result #return result
        
            
        
#DFS
#TC: O(n)
#SC: O(h) - height of the tree is 'h'
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans 
        
    def dfs(self,node, i):  

        if not node: return   

        #only the values that are greater than the depth of right, is appended inside ans after right is traversed
        if i >= len(self.ans): 
            self.ans.append(node.val) 
        
        #every time increase the level as you go through nodes
        self.dfs(node.right, i+1) 
        self.dfs(node.left, i+1) 