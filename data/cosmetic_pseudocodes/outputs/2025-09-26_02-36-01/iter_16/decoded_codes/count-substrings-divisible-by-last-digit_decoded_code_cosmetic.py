class Solution:
    def countSubstrings(self, s: str) -> int:
        length_holder = len(s)
        result_counter = 0
        outer_index = 0
        while outer_index < length_holder:
            accumulator = 0
            inner_index = outer_index
            while inner_index < length_holder:
                digit_val = ord(s[inner_index]) - ord('0')
                accumulator = accumulator * 10 + digit_val
                if digit_val != 0 and accumulator % digit_val == 0:
                    result_counter += 1
                inner_index += 1
            outer_index += 1
        return result_counter