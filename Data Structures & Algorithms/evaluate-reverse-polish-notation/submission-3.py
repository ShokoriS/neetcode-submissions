import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            
        stack = []

        # Map operators to functions
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)  # truncate toward zero
        }

        for token in tokens:
            if token.lstrip('-').isdigit():  # handles negative numbers
                stack.append(int(token))
            elif token in ops:
                right = stack.pop()
                left = stack.pop()
                stack.append(ops[token](left, right))

        return int(stack.pop()) if stack else None

