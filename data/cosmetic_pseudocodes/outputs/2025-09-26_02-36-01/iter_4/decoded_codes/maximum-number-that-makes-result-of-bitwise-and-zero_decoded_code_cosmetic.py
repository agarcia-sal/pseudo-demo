class Solution:
    def maxNumber(self, n: int) -> int:
        if n == 1:
            return 0

        bit_marker = 1
        while True:
            if bit_marker > n:
                break
            bit_marker *= 2

        adjusted_bit = bit_marker // 2
        temp_result = adjusted_bit - 1
        return temp_result