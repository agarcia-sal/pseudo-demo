class Solution:
    def maxSubstringLength(self, s: str) -> int:
        ZERO = 0
        ONE = 1
        frequencies_full = {}
        maximum_length = -(ONE + ZERO)

        # compute frequency count for all characters of s
        index_outer = ZERO
        while index_outer < (len(s) - ONE):
            char_outer = s[index_outer]
            if char_outer in frequencies_full:
                frequencies_full[char_outer] += ONE
            else:
                frequencies_full[char_outer] = ONE
            index_outer += ONE

        # handle last character frequency
        last_char = s[len(s) - ONE]
        if last_char in frequencies_full:
            frequencies_full[last_char] += ONE
        else:
            frequencies_full[last_char] = ONE

        start_pos = ZERO
        while start_pos <= (len(s) - ONE):
            frequencies_current = {}
            end_pos = start_pos
            while True:
                if end_pos > (len(s) - ONE):
                    break

                current_char = s[end_pos]
                if current_char in frequencies_current:
                    frequencies_current[current_char] += ONE
                else:
                    frequencies_current[current_char] = ONE

                condition_met = True
                keys_list = list(frequencies_current.keys())
                key_index = 0
                while key_index < len(keys_list):
                    char_key = keys_list[key_index]
                    if frequencies_current[char_key] < frequencies_full[char_key]:
                        condition_met = False
                        break
                    key_index += ONE

                if condition_met:
                    if len(frequencies_current) < len(frequencies_full):
                        candidate_length = (end_pos - start_pos) + ONE
                        if candidate_length > maximum_length:
                            maximum_length = candidate_length

                end_pos += ONE

            start_pos += ONE

        return maximum_length