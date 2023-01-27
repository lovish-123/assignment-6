class ParenthesesChecker:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        stack = []
        for char in self.string:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack

s = ParenthesesChecker("(){}[]")
print(s.is_valid()) # True

s = ParenthesesChecker("[({])}")
print(s.is_valid()) # False

s = ParenthesesChecker("({[{}]})")
print(s.is_valid()) # True