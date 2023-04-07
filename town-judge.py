#TC: O(n) 
#SC: O(n)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
         
            
        h = [0]*n #create an array of people
        
        for x,y in trust:
            h[x-1] -= 1 #if the person trusts someone, his credibility decreases
            h[y-1] +=1  #if the person is trusted someone, his credibility increases 

        for i in range(len(h)): 

            if h[i] == n-1:  #if the credibility is equal to the number of people - 1, then everybody except him trusts him

                return i+1 #return the index + 1 as answer (person)

        return -1 #else return -1, if there's no town judge
                    
            
            