#TC: O(n log n) 
#SC: O(1)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)-1    
        #sort the array
        nums.sort()

        result = [] #have a resultant array

        for i in range(n-1):
            if i>=1 and nums[i]==nums[i-1]: #just continue if you have duplicates
                continue

            j = i+1  #j pointer starts after i
            k = n #k stands at the end
            target = 0 - nums[i] #target will be the negative complement of the current element

            while j<k:
                if nums[j] + nums[k] == target:  #if j element and the k element gives the target, return all three indices
                    result.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j] == nums[j+1]: #adjust j pointer if you have duplicates
                        j+=1

                    while j<k and nums[k] == nums[k-1]: #adjust k pointer if you have duplicates
                        k-=1

                    #go to the next new element
                    j+=1
                    k-=1

                else:  #traverse k if target is lesser than the sum of current elements or else increment j
                    if target < (nums[j]+nums[k]):
                        k-=1
                    else:
                        j+=1

        return result #now return result