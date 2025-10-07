from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_list = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        substring_found = False
        position = 0
        max_position = len(current_string) - len(substring)
        while position <= max_position and not substring_found:
            match = True
            substring_index = 0
            while substring_index < len(substring) and match:
                if current_string[position + substring_index] != substring[substring_index]:
                    match = False
                substring_index += 1
            if match:
                substring_found = True
            else:
                position += 1
        if substring_found:
            filtered_list.append(current_string)
        index += 1
    return filtered_list