def rotateString(self, s: str, goal: str) -> bool:
    result = False
    for i in range(len(s)):
        if goal == (s[i:]+s[:i]):
            result = True
    
    return result