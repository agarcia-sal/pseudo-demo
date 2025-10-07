from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:

    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_depth_value = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_depth_value:
                    max_depth_value = depth_counter
            else:
                depth_counter -= 1
        return max_depth_value

    substrings: List[str] = []
    cursor = 0
    start_pos = 0
    length = len(parentheses_string)
    while cursor <= length:
        if cursor == length or parentheses_string[cursor] == ' ':
            if start_pos < cursor:
                substrings.append(parentheses_string[start_pos:cursor])
            start_pos = cursor + 1
        cursor += 1

    result_list: List[int] = []
    for substring in substrings:
        if substring != '':
            result_list.append(parse_paren_group(substring))
    return result_list