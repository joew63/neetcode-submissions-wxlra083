class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for num in range(len(s)):
            if len(stack) == 0 and (s[num] == "}" or s[num] == "]" or s[num] == ")"):
                return False
            if s[num] == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
            elif s[num] == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            elif s[num] == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            else:
                stack.append(s[num])
        if len(stack) == 0:
            return True
        else:
            return False