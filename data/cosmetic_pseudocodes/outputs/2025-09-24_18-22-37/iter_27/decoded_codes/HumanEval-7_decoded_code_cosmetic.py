from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_element: str = list_of_strings[idx]
        substring_found_flag: bool = False
        char_position: int = 0
        limit: int = len(current_element) - len(substring_value)
        while char_position <= limit and not substring_found_flag:
            match_flag: bool = True
            offset: int = 0
            while offset < len(substring_value) and match_flag:
                if current_element[char_position + offset] != substring_value[offset]:
                    match_flag = False
                offset += 1
            if match_flag:
                substring_found_flag = True
            char_position += 1
        if substring_found_flag:
            filtered_collection.append(current_element)
        idx += 1
    return filtered_collection