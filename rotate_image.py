#TC: O(n*n) 
#SC: O(1)



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        
        #transposing the matrix
        size = len(matrix)
        for i in range(size):
            for j in range(i+1, size):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]  
                
        #reversing the rows using two pointers
        for i in range(size): 
            start, end = 0, len(matrix[i])-1
            while start< end:
                matrix[i][start], matrix[i][end] = matrix[i][end] , matrix[i][start]
                start += 1
                end -= 1
        