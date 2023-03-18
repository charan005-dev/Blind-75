#TC: O(n) 
#SC: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         
        h = {}  # create a hashmap
        
        for i in nums: 
            if i not in h:  #if it's not in hashmap, invoke it's value as 1 or else increase it
                h[i] = 1  
            else: 
                h[i] += 1
                
            if h[i] >= 2: #if the count is greater or equal to 2, return true
                
                return True 
            
        return False