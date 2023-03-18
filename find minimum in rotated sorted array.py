#TC: O(log n)
#SC: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        l,r = 0, len(nums)-1 #have left and right pointer
        
        while l < r: #loop runs until left and right pointer meet
            m = (l+r)//2 #find the mid
            if nums[m] >= nums[r]: #if mid element is greater or equal to the right element, we have to traverse the left to mid+1 else traverse r to mid
                l = m + 1
            else:
                r = m
        return nums[l] #left pointer stands in our answer