from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_found = 0
        index_tracker = 0
        string_length = len(group_string)
        while index_tracker < string_length:
            current_char = group_string[index_tracker]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > max_depth_found:
                    max_depth_found = depth_counter
            else:
                depth_counter -= 1
            index_tracker += 1
        return max_depth_found

    temp_groups: List[str] = []
    substring_start = 0
    position = 0
    total_length = len(parentheses_string)
    while position <= total_length:
        if position == total_length or parentheses_string[position] == ' ':
            substring_length = position - substring_start
            if substring_length > 0:
                substring_extract = parentheses_string[substring_start:position]
                temp_groups.append(substring_extract)
            substring_start = position + 1
        position += 1

    result_list: List[int] = []
    for element in temp_groups:
        if element != '':
            depth_result = parse_paren_group(element)
            result_list.append(depth_result)

    return result_list