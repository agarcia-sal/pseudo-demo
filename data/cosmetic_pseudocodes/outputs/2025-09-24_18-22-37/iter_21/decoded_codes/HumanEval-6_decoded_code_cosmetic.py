from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_found = 0
        length_of_group = len(group_string)
        index = 0
        while index < length_of_group:
            current_char = group_string[index]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > max_depth_found:
                    max_depth_found = depth_counter
            else:
                depth_counter -= 1
            index += 1
        return max_depth_found

    splitted_groups = parentheses_string.split(' ')
    result_list: List[int] = []
    for single_group in splitted_groups:
        if single_group != '':
            result_list.append(parse_paren_group(single_group))
    return result_list