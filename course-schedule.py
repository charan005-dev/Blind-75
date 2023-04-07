#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list) #Initialize adjacency matrix as defaultdict which has values as lists
        q = deque() #Initialize deque
        indegree = [0]*numCourses   #Initialize an idegree array initially with all zeroes
        Scourse = 0   #Initially Scourse will be 0
        
        
        for course, prereq, in prerequisites:   #For every course and prereq in prerequisites
            adj[prereq].append(course)  #Append the course in to adj for the corresponding prereq
            indegree[course] += 1   #Increment 1 for that course in the indegree array everytime a course is added to the prereq
            

        for i in range(len(indegree)):  #Continue till the length of indegree   
            if indegree[i] == 0:    #If the indegree[i] is 0, Append the index to the q
                q.append(i) 
                
        if not q:   #If there is no values in q Return False
            return False
        
        while q:    #Continu till the q is empty
            curr = q.popleft()  #curr will be the first element in the queue
            Scourse += 1  #Add Scourse by 1 every time a course is completed
            for dependent in adj[curr]: 
                indegree[dependent] -= 1    #Decrement the value of that course in the indegree array by 1
                if indegree[dependent] == 0:    #If the value of that dependent in indegree is 0 append it to the queue
                    q.append(dependent)
                    
        if Scourse == numCourses: #If the Scourse is equal to the numCourses then return True
            return True
        return False    #Return false