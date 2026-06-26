class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs= {')': '(', '}': '{', ']': '['}
        for i in s:
            if i == '(' or i== '{' or i== '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1]==pairs[i]:
                    stack.pop()
                else:
                    return False
                
        return not stack
                
