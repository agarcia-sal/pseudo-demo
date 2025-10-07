from collections import Counter
import string

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        letter_count = Counter(s)
        letter_count.pop('?', None)

        question_marks = [i for i, char in enumerate(s) if char == '?']

        replacement_chars = []
        for _ in question_marks:
            min_count = float('inf')
            min_char = None
            for char in string.ascii_lowercase:
                count = letter_count.get(char, 0)
                if count < min_count:
                    min_count = count
                    min_char = char
            replacement_chars.append(min_char)
            letter_count[min_char] = letter_count.get(min_char, 0) + 1

        replacement_chars.sort()

        s_list = list(s)
        for idx, char in zip(question_marks, replacement_chars):
            s_list[idx] = char

        return ''.join(s_list)