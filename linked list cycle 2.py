#TC: O(n) 
#SC: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 

        if not head: 
            return head 

        slow = head 
        fast = head 
        cycle = False 

        while fast != None and fast.next!=None:  #traverse until fast and next to fast is not None
            slow = slow.next  #slow pointer jumps one at a time
            fast = fast.next.next #fast pointer jumps twice

            if slow == fast:  #if slows equals fast, then there's a cycle
                cycle = True  
                break 

        if not cycle:  #if, there's no cycle, return null
            return None 

        slow = head #now, slow pointer is our new head
        while slow!=fast: #traverse until slow equals fast
            slow = slow.next  #now, slow goes by one and fast goes by one
            fast = fast.next 
        return slow #when loop exits, slow pointer will be in the start of the cycle