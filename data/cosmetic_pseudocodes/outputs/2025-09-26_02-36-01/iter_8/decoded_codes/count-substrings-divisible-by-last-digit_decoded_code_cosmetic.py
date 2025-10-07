class Solution:
    def countSubstrings(self, s: str) -> int:
        length_s = len(s)
        accumulator = 0
        outerIndex = 0
        while True:
            if outerIndex > length_s - 1:
                break
            multiplier_accum = 0
            innerIndex = outerIndex
            while True:
                if innerIndex > length_s - 1:
                    break
                digit_char = s[innerIndex]
                digit_val = ord(digit_char) - ord('0')
                multiplier_accum = multiplier_accum * 10 + digit_val
                if digit_val != 0 and multiplier_accum % digit_val == 0:
                    accumulator += 1
                innerIndex += 1
            outerIndex += 1
        return accumulator