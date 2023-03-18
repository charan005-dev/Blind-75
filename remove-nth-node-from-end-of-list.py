#TC: O(n) 
#SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  

        count = 0 
        dummy = ListNode("dummy", head) #create a dummy node
        slow = dummy #slow pointer points to dummy
        fast = dummy #right pointer points to dummy 

        while count < n:  #traverse until count is less than n
            fast = fast.next #increment the fast pointer by 1 
            count+=1 #increment the count by 1

        while fast.next != None:  #traverse until the next of fast is not equal to null
            slow = slow.next #increment the slow by one
            fast = fast.next #increment the fast by one

        slow.next = slow.next.next #point your slow.next to one place next as we are deleting the node in between

        return dummy.next #dummy.next points to the head
