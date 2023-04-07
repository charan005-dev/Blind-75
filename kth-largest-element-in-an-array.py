#TC: O(n) 
#SC:O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = [] #open a heap
        nk = len(nums) - k + 1
        for num in nums:
            heappush(hp,-num) #push as negatives
            if len(hp)>nk: #maintain k size, if exceeds, pop it
                heappop(hp)

        return -hp[0]
