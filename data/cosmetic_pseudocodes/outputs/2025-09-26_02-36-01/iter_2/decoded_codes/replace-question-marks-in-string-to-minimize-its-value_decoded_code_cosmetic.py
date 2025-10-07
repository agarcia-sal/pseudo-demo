from collections import Counter

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        char_frequencies = Counter(s)
        if '?' in char_frequencies:
            del char_frequencies['?']

        positions = []
        pos_index = 0
        while pos_index < len(s):
            current_char = s[pos_index]
            if current_char == '?':
                positions.append(pos_index)
            pos_index += 1

        substitutes = []
        for _ in positions:
            least_frequency = float('inf')
            character_to_use = None
            ascii_code = 97  # 'a'
            while ascii_code <= 122:  # 'z'
                alphabet_char = chr(ascii_code)
                frequency_count = char_frequencies.get(alphabet_char, 0)
                if frequency_count < least_frequency:
                    least_frequency = frequency_count
                    character_to_use = alphabet_char
                ascii_code += 1
            substitutes.append(character_to_use)
            char_frequencies[character_to_use] += 1

        substitutes.sort()
        array_of_chars = list(s)
        idx = 0
        while idx < len(positions):
            replacement_pos = positions[idx]
            replacement_char = substitutes[idx]
            array_of_chars[replacement_pos] = replacement_char
            idx += 1

        return ''.join(array_of_chars)