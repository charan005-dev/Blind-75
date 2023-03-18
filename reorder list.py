#TC: O(n) 
#SC: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """ 

        mid = self.findMid(head) #find the mid
        midNext = mid.next 
        mid.next = None 
        headB = self.reverse(midNext) #reverse the list formed using mid next
        headA = head
        self.mergeLinkedLists(headA,headB) #now merge both the lists


    def findMid(self, head): 

        slow = head 
        fast = head 

        while fast.next!=None and fast.next.next != None: #finding mid using slow and fast pointer
            slow = slow.next 
            fast = fast.next.next 

        return slow 

    def reverse(self,head):  #function to reverse alinked list
        prev = None 
        curr = head 

        while curr: #traverse until there is current node
            temp = curr.next #initilize temp to current.next
            curr.next = prev #now curr.next points to prev
            prev = curr #now prev points curr and curr points again to temp
            curr = temp 
        return prev 

    def mergeLinkedLists(self,head1,head2): #function to merge two linked lists
        p1 = head1 
        p2 = head2 
        while  p2: #traverse until p2 is there
            temp = p1.next  #initially temp points to p1.next
            p1.next = p2 
            p2 = p2.next 
            p1.next.next = temp #p1.next.next gets assigned to temp
            p1 = temp  #now p1 is assigned to temp again



