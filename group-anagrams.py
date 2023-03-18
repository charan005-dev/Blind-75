#TC: O(len(arr) * len(str in array)) 
#SC: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h={}
        res=[]
        for word in strs:
            key = self.hashcode(word) #create a unique hashcode for every word in the given array
            if key not in h:
                h[key] = [word] #set the key as the hashcode and text as current value if not in hashmap
            else:
                h[key].append(word) #or else, kjust append the word to the hashmap
        
        
        for k,v in h.items(): #now send all the values to resultant array
            res.append(v)
            
        return res #return res
        
        
        
    def hashcode(self,s):  #function to generate hashcode
        c = 0
        for i in s: 
            c += ord(i) ** 5
        return c