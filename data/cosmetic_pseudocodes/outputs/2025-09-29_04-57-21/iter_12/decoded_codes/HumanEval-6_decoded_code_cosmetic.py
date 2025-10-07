from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        active_depth = 0
        deepest_depth = 0
        index = 0
        length = len(group_string)

        while index < length:
            symbol = group_string[index]
            if symbol == '(':
                active_depth += 1
                if active_depth > deepest_depth:
                    deepest_depth = active_depth
            else:
                active_depth -= 1
            index += 1

        return deepest_depth

    splitted_groups: List[str] = []
    temp_str = ""
    cursor = 0
    str_len = len(parentheses_string)

    while cursor < str_len:
        curr_char = parentheses_string[cursor]
        if curr_char == ' ':
            if len(temp_str) > 0:
                splitted_groups.append(temp_str)
                temp_str = ""
        else:
            temp_str += curr_char
        cursor += 1

    if len(temp_str) > 0:
        splitted_groups.append(temp_str)

    results_list: List[int] = []
    for single_group in splitted_groups:
        if len(single_group) > 0:
            results_list.append(parse_paren_group(single_group))

    return results_list