class Solution:
    def countSubstrings(self, s: str) -> int:
        length_s = len(s)
        count_substrings = 0
        index_start = 0
        while index_start < length_s:
            number_accumulator = 0
            index_end = index_start
            while index_end < length_s:
                digit_char = s[index_end]
                digit_value = int(digit_char)
                number_accumulator = number_accumulator * 10 + digit_value
                if digit_value != 0:
                    if number_accumulator % digit_value == 0:
                        count_substrings += 1
                index_end += 1
            index_start += 1
        return count_substrings