#TC: O(n) 
#SC: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        gmax = -10 #set your global max as -10
         
        cmin = 1 #current min as 1
        cmax = 1 #current max as 2
        
        for i in nums:  #at every point, calculate the max and min of (current min, current max and current element) and update cmax and cmin

            cmax,cmin =  max(cmin*i, cmax*i, i), min(cmin*i, cmax*i, i) 
            
            gmax = max(cmax,gmax) #update the global max with cmax if it's greater
             
        return gmax #return the global max
            