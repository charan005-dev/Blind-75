class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        iset = set() #create a set for row
        jset = set() #create a set for column
        m = len(matrix)
        n = len(matrix[0])
        flag = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    iset.add(i) #if the element is 0, add the row to he sety
                    jset.add(j) #if the element is 0, add the column to the set
                    flag=True       
            if flag:
                matrix[i] = [0]*n #check the flag and make the entire row as 0's
                flag=False

        for i in range(m):
            if i not in iset:
                for j in jset:
                     matrix[i][j]=0 #check for column element and make it as 0