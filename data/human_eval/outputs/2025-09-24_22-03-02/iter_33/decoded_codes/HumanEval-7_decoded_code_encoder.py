from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_list = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        contains_substring = False
        substring_index = 0
        substring_length = len(substring)
        current_string_length = len(current_string)
        while substring_index <= current_string_length - substring_length and not contains_substring:
            match = True
            char_index = 0
            while char_index < substring_length and match:
                if current_string[substring_index + char_index] != substring[char_index]:
                    match = False
                char_index += 1
            if match:
                contains_substring = True
            substring_index += 1
        if contains_substring:
            filtered_list.append(current_string)
        index += 1
    return filtered_list