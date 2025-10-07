from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_list = []
    index = 0
    length_of_strings = len(strings)
    while index < length_of_strings:
        current_string = strings[index]
        contains_substring = False
        substring_index = 0
        length_of_current_string = len(current_string)
        length_of_substring = len(substring)
        while substring_index <= length_of_current_string - length_of_substring and not contains_substring:
            match_index = 0
            is_match = True
            while match_index < length_of_substring and is_match:
                if current_string[substring_index + match_index] != substring[match_index]:
                    is_match = False
                match_index += 1
            if is_match:
                contains_substring = True
            substring_index += 1
        if contains_substring:
            filtered_list.append(current_string)
        index += 1
    return filtered_list