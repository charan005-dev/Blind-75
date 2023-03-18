#TC: O(n) 
#SC:O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        p1 = 0 
        p2 = len(height)-1 
        maxi = 0
        
        while p1<p2: 
            
            pivot = min(height[p1], height[p2])   #pivot will be the minimum between the heights where p1 is and height where p2 is
            
            
            res = pivot * (p2-p1)  #the current result will be the product of pivot and the difference between p1 and p2
            
            if res >= maxi:  #update the maximum area with current res
                
                maxi = res  
                
                
            if pivot == height[p1]:  #increment p1 if pivot equals current height, else decrement p2
                
                p1+=1 
                
            else: 
                
                p2-=1 
                
        return maxi
                
            
                