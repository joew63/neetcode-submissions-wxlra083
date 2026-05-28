class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(int(first) + int(second))
                elif token == "-":
                    stack.append(int(first) - int(second))
                elif token == "*":
                    stack.append(int(first) * int(second))
                elif token == "/":
                    # if second != "0":
                    stack.append(int(int(first) / int(second)))
                    # else:
                    #     stack.append(0)
            else:
                stack.append(int(token))
        return stack[0]