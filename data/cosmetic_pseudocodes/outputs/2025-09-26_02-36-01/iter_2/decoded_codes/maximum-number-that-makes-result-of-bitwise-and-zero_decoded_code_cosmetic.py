class Solution:
    def maxNumber(self, n: int) -> int:
        if n == 1:
            return 0

        leadingBit = 1
        while n >= leadingBit:
            leadingBit <<= 1  # equivalent to leadingBit = leadingBit * 2

        leadingBit >>= 1  # divide by 2

        resultNum = leadingBit - 1
        return resultNum