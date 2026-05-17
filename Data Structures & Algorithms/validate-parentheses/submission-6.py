class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        stack = []

        for char in s:
            
            if char not in mapping:
                stack.append(char)
            else:
                if len(stack)==0 or stack[-1]!=mapping[char]:
                    return False
                else:
                    stack.pop()

        return (len(stack)==0)