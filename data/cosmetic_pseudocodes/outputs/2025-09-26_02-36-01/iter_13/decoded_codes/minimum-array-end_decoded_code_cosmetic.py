class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def bin_and(a: int, b: int) -> int:
            res = 0
            bit_mask = 1
            for _ in range(32):
                bitA = (a // bit_mask) % 2
                bitB = (b // bit_mask) % 2
                if bitA == 1 and bitB == 1:
                    res += bit_mask
                bit_mask <<= 1
            return res

        def canConstruct(max_value: int) -> bool:
            temp_val = x
            tally = 1
            while temp_val < max_value:
                temp_val += 1
                if bin_and(temp_val, x) == x:
                    tally += 1
                    if tally == n:
                        return True
            return False

        lowBound = x
        highBound = 2 * 10**8  # equivalent to 2*10^8

        while lowBound < highBound:
            median = (lowBound + highBound) // 2
            if canConstruct(median):
                highBound = median
            else:
                lowBound += 1

        return lowBound