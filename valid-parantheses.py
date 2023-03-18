#TC: O(n) 
#SC:O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = []
    
        for c in s:
        
        # If c is an open bracket -> add it to the stack
            if c in ('(', '{', '['): 
                stack.append(c)
            
            else:
            # If the stack is empty and c is a closed bracket -> the parentheses are invalid
                if stack == []: 
                    return False
            
            # If the open bracket on top of the stack matches c -> close it (remove it from the top of the stack)
                elif c == ')' and stack[-1] == '(': 
                    stack.pop(-1)
                
                elif c == '}' and stack[-1] == '{':
                    stack.pop(-1)
            
                elif c == ']' and stack[-1] == '[':
                    stack.pop(-1)
            
            # If the open bracket on top of the stack does not match c -> the parentheses are invalid
                else:
                    return False
    
    # If the stack is now empty -> the parentheses are valid
        if stack == []: 
            return True
    
    # If there is an open bracket still in the stack -> the parentheses are invalid
        else: 
            return False