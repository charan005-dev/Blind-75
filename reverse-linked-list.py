#TC:O(n) 
#SC:O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  

        prev = None #set the prev pointer to none
        curr = head  #now set the curr node to head

        while curr!= None: #traverse until current node is not equal to null
            temp = curr.next  #temp initially points to next of current
            curr.next = prev  #next of current becomes prev now 
            prev = curr #initial previous is going to be current now
            curr = temp #now current points to temp

        return prev #previous pointer points to the head

        