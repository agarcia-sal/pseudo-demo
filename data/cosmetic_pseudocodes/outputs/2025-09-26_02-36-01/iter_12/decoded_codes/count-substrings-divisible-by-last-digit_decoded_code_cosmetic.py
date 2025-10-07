class Solution:
    def countSubstrings(self, s: str) -> int:
        length_s = 0
        while True:
            if length_s >= len(s):
                break
            length_s += 1

        count_result = 0

        def helperOuter(idx_outer: int):
            nonlocal count_result
            if idx_outer >= length_s:
                return

            accumulator_val = 0

            def helperInner(idx_inner: int):
                nonlocal accumulator_val, count_result
                if idx_inner >= length_s:
                    return

                char_at_inner = s[idx_inner]

                def charToInt(c: str) -> int:
                    return ord(c) - ord('0')

                digit_val = charToInt(char_at_inner)
                accumulator_val = accumulator_val * 10 + digit_val

                if digit_val != 0 and accumulator_val % digit_val == 0:
                    count_result += 1

                helperInner(idx_inner + 1)

            helperInner(idx_outer)
            helperOuter(idx_outer + 1)

        helperOuter(0)
        return count_result