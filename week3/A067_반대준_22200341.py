def removeDuplicates(self, s: str) -> str:
    stack = [s[0]]
    s = s[1:]
    for i in s:
        
        if (stack and stack[-1]==i):
                stack.pop()
        else:
            stack.append(i)

    return "".join(stack)
