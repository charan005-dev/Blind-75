#TC: O(m*n) 
#SC: O(1)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # always have m as number of rows and n as number of columns
        m = len(text1) 
        n = len(text2) 

        #grid = [[0 for i in range(n+1)] for j in range(m+1)] 
        
        prev = [0]*(m+1) 
        
        #always use i to iterate over rows(m), and j to iterate over columns(j)   
        #jump diagonally when elementsmatch or else go to the max of right and down
        
        for i in range(n-1,-1,-1):  
            curr = [0]*(m+1)
            for j in range(m-1,-1,-1): 
                if text2[i] == text1[j]: 
                    curr[j] =  1 + prev[j+1] 
                else: 
                    curr[j] = max(curr[j+1], prev[j]) 
                    
            prev = curr  
            
        return curr[0]
