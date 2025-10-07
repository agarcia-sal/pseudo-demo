class Solution:
    def countSubstrings(self, s: str) -> int:
        length_value = len(s)
        substring_count = 0
        outer_index = 0
        while outer_index <= length_value - 1:
            accumulator = 0
            inner_idx = outer_index
            while inner_idx <= length_value - 1:
                digit_value = int(s[inner_idx])
                accumulator = accumulator * 10 + digit_value
                if digit_value != 0 and ((accumulator - digit_value + digit_value) % digit_value) == 0:
                    substring_count += 1
                inner_idx += 1
            outer_index += 1
        return substring_count