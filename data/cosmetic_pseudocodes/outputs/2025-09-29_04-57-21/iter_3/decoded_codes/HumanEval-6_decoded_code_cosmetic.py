from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        deepest_level = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > deepest_level:
                    deepest_level = depth_counter
            else:
                depth_counter -= 1
        return deepest_level

    splitted_groups: List[str] = []
    temp_index = 0
    total_length = len(parentheses_string)

    while temp_index < total_length:
        if parentheses_string[temp_index] != ' ':
            start_pos = temp_index
            while temp_index < total_length and parentheses_string[temp_index] != ' ':
                temp_index += 1
            splitted_groups.append(parentheses_string[start_pos:temp_index])
        else:
            temp_index += 1

    result_list: List[int] = [parse_paren_group(group_elem) for group_elem in splitted_groups if group_elem]
    return result_list