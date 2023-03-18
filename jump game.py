#TC: O(n) 
#SC: O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = len(nums)-1  #d stands at the end

        for i in range(len(nums)-2,-1,-1): #come from backwards
            if i + nums[i] >=d: #if the sum of current index and current element is greater than or equal to the length of nums - 1, d points to current index
                d = i

        return d == 0 #if d becomes zero, then it's true that we can jump to the end or else false