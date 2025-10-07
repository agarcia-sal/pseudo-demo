from collections import Counter
import math

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counts = Counter(s)
        if '?' in counts:
            del counts['?']

        question_positions = [i for i, ch in enumerate(s) if ch == '?']

        replacements = []
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

        for pos in question_positions:
            lowest_freq = math.inf
            chosen_char = None
            for letter in ALPHABET:
                freq = counts.get(letter, 0)
                if freq < lowest_freq:
                    lowest_freq = freq
                    chosen_char = letter
            replacements.append(chosen_char)
            counts[chosen_char] = counts.get(chosen_char, 0) + 1

        replacements.sort()
        char_array = list(s)

        for i, pos in enumerate(question_positions):
            char_array[pos] = replacements[i]

        return ''.join(char_array)