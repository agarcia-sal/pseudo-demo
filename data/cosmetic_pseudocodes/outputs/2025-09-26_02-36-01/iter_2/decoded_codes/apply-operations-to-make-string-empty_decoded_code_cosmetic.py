class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        frequency_map = {}
        index_counter = 0
        while index_counter < len(s):
            current_char = s[index_counter]
            if current_char not in frequency_map:
                frequency_map[current_char] = 1
            else:
                frequency_map[current_char] += 1
            index_counter += 1

        highest_count = 0
        for key_key in frequency_map.keys():
            if frequency_map[key_key] > highest_count:
                highest_count = frequency_map[key_key]

        frequent_chars = set()
        for symbol in frequency_map.keys():
            if frequency_map[symbol] == highest_count:
                frequent_chars.add(symbol)

        collected_chars = []
        rev_index = len(s) - 1
        while rev_index >= 0:
            char_here = s[rev_index]
            if char_here in frequent_chars:
                collected_chars.append(char_here)
                frequent_chars.remove(char_here)
            rev_index -= 1

        output_string = ''
        back_index = len(collected_chars) - 1
        while back_index >= 0:
            output_string += collected_chars[back_index]
            back_index -= 1

        return output_string