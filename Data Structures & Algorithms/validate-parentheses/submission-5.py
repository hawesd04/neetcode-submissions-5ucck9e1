class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = False
        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                stack.append(char)
                check = True
            else:
                if (stack):
                    top = stack.pop()
                else:
                    top = 'empty'
                
                if (char == ')' and top != '('):
                    return False
                elif (char == ']' and top != '['):
                    return False
                elif (char == '{' and top != '}'):
                    return False
        
        if stack or check == False:
            return False
        return True