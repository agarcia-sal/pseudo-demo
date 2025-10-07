class Solution:
    def countSubstrings(self, s: str) -> int:
        length_of_s = len(s)
        substrings_count = 0

        for start_index in range(length_of_s):
            number_accumulator = 0
            for end_index in range(start_index, length_of_s):
                digit_char = s[end_index]
                digit_value = ord(digit_char) - ord('0')
                number_accumulator = number_accumulator * 10 + digit_value
                if digit_value != 0 and (number_accumulator % digit_value) == 0:
                    substrings_count += 1

        return substrings_count