class Solution:
    def countSubstrings(self, t: str) -> int:
        m = len(t)
        sum_result = 0

        def evaluateDivisibleSegment(startIdx: int) -> int:
            def helper(idx: int, acc: int) -> int:
                if idx > m - 1:
                    return 0  # no more substrings, no increment
                digit_val = ord(t[idx]) - ord('0')
                new_number = acc * 10 + digit_val

                def isDivisible(num: int, d: int) -> bool:
                    return d != 0 and num % d == 0

                if isDivisible(new_number, digit_val):
                    return helper(idx + 1, new_number) + 1
                else:
                    return helper(idx + 1, new_number)

            return helper(startIdx, 0)

        p = 0
        while p < m:
            sum_result += evaluateDivisibleSegment(p)
            p += 1

        return sum_result