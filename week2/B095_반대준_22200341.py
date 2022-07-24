def reverseBits(n: int) -> int:
    num = 0

    for i in range(32):
        num <<= 1
        num |= n & 1
        n >>= 1

    return num