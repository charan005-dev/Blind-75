#TC: O(n) 
#SC: O(len(t))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t='' 
        for i in s: 
            if (ord(i) >64 and ord(i) < 91): #build the t string with changing the alphabets available to lower case if it's in capital letters or else numbers or small characters
                t+=i.lower() 
            elif (ord(i) >=97 and ord(i) < 123 ) or  (ord(i)>47 and ord(i)<58):  
                t+=i 
        
        if  t==t[::-1]:  #now check with string reversing
            return True
        else: 
            return False