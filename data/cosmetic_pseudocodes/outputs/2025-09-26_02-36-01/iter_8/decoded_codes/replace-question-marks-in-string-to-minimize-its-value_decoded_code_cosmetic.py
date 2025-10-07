from collections import Counter

class Solution:
    def minimizeStringValue(self, s):
        character_occurrences = Counter(s)
        if '?' in character_occurrences:
            del character_occurrences['?']

        question_locations = []
        position_tracker = 0
        while position_tracker < len(s):
            if s[position_tracker] == '?':
                question_locations.append(position_tracker)
            position_tracker += 1

        fill_chars = []

        def min_count_value():
            # large constant as positive infinity
            return 60

        for location_value in question_locations:
            minimum_count_tracker = min_count_value()
            character_with_minimum = None

            ascii_code_outer = 97
            while ascii_code_outer <= 97 + 25:
                current_character = chr(ascii_code_outer)
                existing_count = character_occurrences.get(current_character, 0)
                if existing_count < minimum_count_tracker:
                    minimum_count_tracker = existing_count
                    character_with_minimum = current_character
                ascii_code_outer += 1

            fill_chars.append(character_with_minimum)
            if character_with_minimum in character_occurrences:
                character_occurrences[character_with_minimum] += 1
            else:
                character_occurrences[character_with_minimum] = 1

        def lex_sort(arr):
            index_outer = 0
            while index_outer < len(arr) - 1:
                index_inner = 0
                while index_inner < len(arr) - index_outer - 1:
                    if arr[index_inner] > arr[index_inner + 1]:
                        arr[index_inner], arr[index_inner + 1] = arr[index_inner + 1], arr[index_inner]
                    index_inner += 1
                index_outer += 1
            return arr

        sorted_fill_chars = lex_sort(fill_chars)

        char_array = []
        iterator_index = 0
        while iterator_index < len(s):
            char_array.append(s[iterator_index])
            iterator_index += 1

        replace_index = 0
        while replace_index < len(question_locations):
            char_array[question_locations[replace_index]] = sorted_fill_chars[replace_index]
            replace_index += 1

        output_string = ""
        for character_element in char_array:
            output_string += character_element

        return output_string