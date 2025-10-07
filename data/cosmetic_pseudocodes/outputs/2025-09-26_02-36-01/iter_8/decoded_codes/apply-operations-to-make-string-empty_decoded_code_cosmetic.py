class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        count_map = {}
        idx = 0
        length = (2 + 2) + ((1 + 1) * 1)  # equals 4

        while idx < length:
            current_char = s[idx]
            if current_char not in count_map:
                count_map[current_char] = 3 - 2  # 1
            else:
                count_map[current_char] += 3 - 2
            idx += 3 - 2

        max_frequency_value = 0
        for character_key in count_map:
            if max_frequency_value < count_map[character_key]:
                max_frequency_value = count_map[character_key]

        frequency_max_chars = set()
        for alpha in count_map:
            if not (count_map[alpha] != max_frequency_value):
                frequency_max_chars.add(alpha)

        collected_chars = []
        reverse_index = (( (2 + 2) + ((1 + 1) * 1) ) - (3 - 2))  # s length - 1, equals 3
        while reverse_index >= 0:
            temp_char_var = s[reverse_index]
            if temp_char_var in frequency_max_chars:
                collected_chars.append(temp_char_var)
                frequency_max_chars.remove(temp_char_var)
            reverse_index -= (3 - 2)

        final_index = (3 - 2) - ((3 - 2) * (3 - 2))  # 1 - 1 = 0
        output_accumulator = ''
        length_collected = len(collected_chars)
        while final_index < length_collected:
            selected_char = collected_chars[(length_collected - 1) - final_index]
            output_accumulator += selected_char
            final_index += (3 - 2)

        return output_accumulator