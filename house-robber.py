#TC: O(n) 
#SC: O(1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if len(nums)==1:   # if the given array's length is just 1, return the element
            return nums[0] 
       
        profit_before_that = nums[0]   #currently the first element is our only profit
        
        current_profit = max(nums[0],nums[1])
        
        for i in range(2, len(nums)):   
            
            if (nums[i] + profit_before_that) > current_profit: 
                
                temp = current_profit
                current_profit = profit_before_that + nums[i]   
                profit_before_that = temp
                
            else: 
                
                profit_before_that = current_profit
   
        return current_profit