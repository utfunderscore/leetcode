class Solution:

    def isValid(self, s: str) -> bool:
        closed_to_open = {
            '}': "{",
            ')':"(",
            ']':"["
        }
        stack = []

        for c in s:
            if c in closed_to_open.keys():
                opener = closed_to_open[c]
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if opener != top:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
