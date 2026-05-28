class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(int(first) / int(second)))
            else:
                stack.append(int(token))
        return stack[0]