#TC: O(log n) 
#SC: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2 
            
            if nums[mid] == target: return mid
            
            #either the left side of the mid is sorted or the right side of the mid is sorted 
            #first check with the left side by assigning left pointer to 0 and mid as right pointer and perform binary search
            if nums[mid] >= nums[left]: 
                
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # or else check with the right side by assigning left pointer to mid and the end of array as right pointer and perform binary search
            else:
                
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1