class Solution:
     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {} #open a frequency hashmap
        for num in nums: #have frequency as values
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1 
                
        print(counter_dict)
        return sorted(counter_dict, key = counter_dict.get, reverse=True)[:k] #sort based on items (frequency)