def addBinary(self, a: str, b: str) -> str:
    binarySum = ""
    carry = 0
    a, b = a[::-1], b[::-1]
    
    for i in range(max(len(a), len(b))): 
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0

        binarySum = str((digitA + digitB + carry) % 2) + binarySum
        carry = (digitA + digitB + carry) // 2
    
    if carry:
        binarySum = str(carry) + binarySum
    return binarySum