class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s):
            return True
        
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif len(stack) and brackets[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        if not len(stack):
            return True
        return False