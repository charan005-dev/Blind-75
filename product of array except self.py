#TC: O(n) 
#SC: O(1)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        
        output = [1] * len(nums) #create an output array with 1's filled
        preprod, postprod = 1, 1  #create a preproduct and postproduct pointers
        for i in range(1, len(nums)):  #traverse from the start of the array 
            preprod *= nums[i - 1]  #assign the product of preprod and current element to preprod
            output[i] = preprod #assign the current value of result to output
        for i in range(len(nums) - 2, -1, -1): #traverse from the back of the array and ignore the last element as we are considering rest of the array
            postprod *= nums[i + 1]  #assign the product of postprod and current element to postprod
            output[i] *= postprod #now assign the product of postprod to preprod values already stored
        return output  #return the output
            