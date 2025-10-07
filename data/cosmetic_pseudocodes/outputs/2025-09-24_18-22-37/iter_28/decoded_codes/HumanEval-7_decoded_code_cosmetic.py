from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_strings: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        current_element: str = list_of_strings[index_counter]
        substring_found_flag: bool = False
        max_start: int = len(current_element) - len(substring_value)
        for position in range(max_start + 1):
            segment: str = ""
            char_pos: int = 0
            while char_pos < len(substring_value) and segment != substring_value:
                segment += current_element[position + char_pos]
                char_pos += 1
            if segment == substring_value:
                substring_found_flag = True
                break
        if substring_found_flag:
            filtered_strings.append(current_element)
        index_counter += 1
    return filtered_strings