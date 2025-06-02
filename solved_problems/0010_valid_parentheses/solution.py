class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['[', '{', '(']:
                stack.append(x)
            else:
                if stack:
                    last = stack.pop()
                else:
                    return False
                if x == ')' and last != '(':
                    return False
                elif x == '}' and last != '{':
                    return False
                elif x == ']' and last != '[':
                    return False
        return len(stack) == 0
