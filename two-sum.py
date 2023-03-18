 
#TC : O(n) 
# SC: O(n) 
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hashmap ={}  #create a hashmap
        
        for i in range(len(nums)):   
            
            c = target - nums[i]  #find the complement through difference
            
            
            if c in hashmap: 

                return [hashmap[c],i]   #if complement already present, return its corresponding value and the current index
            
            hashmap[nums[i]] = i  #assigning index as value
             
        
                        
            