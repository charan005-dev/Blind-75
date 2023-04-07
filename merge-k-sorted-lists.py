# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 


#TC: O(n*k) 
#SC: O(n*k)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda a,b : a.val<b.val  #operator overloading

        result = ListNode(0)
        curr = result
        mheap = []

        for listhead in lists: #push all the heads inside the linkedlist
            if listhead:
                heappush(mheap,listhead)

        #heapify operation happens in the heap and we pop the top element and we assign that element as next to dummy node and 
        # we have the next of the popped element as our new element in the heap
        while mheap:
            popele = heappop(mheap)    

            if popele.next:
                heappush(mheap,popele.next)

            curr.next = popele #r(c)->1
            curr = curr.next #r->1(c)

        return result.next #return result.next without including dummy node