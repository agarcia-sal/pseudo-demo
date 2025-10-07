from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_strings = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        found = False
        sub_index = 0
        substring_length = len(substring)
        string_length = len(current_string)
        while sub_index <= string_length - substring_length and not found:
            match = True
            char_index = 0
            while char_index < substring_length and match:
                if current_string[sub_index + char_index] != substring[char_index]:
                    match = False
                char_index += 1
            if match:
                found = True
            sub_index += 1
        if found:
            filtered_strings.append(current_string)
        index += 1
    return filtered_strings