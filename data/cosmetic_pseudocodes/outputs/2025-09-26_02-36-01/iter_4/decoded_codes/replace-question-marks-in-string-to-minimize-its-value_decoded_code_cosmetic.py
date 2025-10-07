from collections import Counter

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        char_frequencies = Counter(s)
        if '?' in char_frequencies:
            del char_frequencies['?']

        positions_of_questions = []
        idx = 0
        length = len(s)
        while idx < length:
            current_char = s[idx]
            if current_char == '?':
                positions_of_questions.append(idx)
            idx += 1

        chars_to_replace = []

        question_index = 0
        while question_index < len(positions_of_questions):
            least_count = float('inf')
            chosen_letter = None
            letter_code = ord('a')
            while letter_code <= ord('z'):
                letter = chr(letter_code)
                count_value = char_frequencies.get(letter, 0)
                if count_value < least_count:
                    least_count = count_value
                    chosen_letter = letter
                letter_code += 1
            chars_to_replace.append(chosen_letter)
            char_frequencies[chosen_letter] = char_frequencies.get(chosen_letter, 0) + 1
            question_index += 1

        chars_to_replace.sort()

        s_as_list = list(s)
        replace_idx = 0
        while replace_idx < len(positions_of_questions):
            pos = positions_of_questions[replace_idx]
            replacement_char = chars_to_replace[replace_idx]
            s_as_list[pos] = replacement_char
            replace_idx += 1

        result_string = ''
        join_index = 0
        while join_index < len(s_as_list):
            result_string += s_as_list[join_index]
            join_index += 1

        return result_string