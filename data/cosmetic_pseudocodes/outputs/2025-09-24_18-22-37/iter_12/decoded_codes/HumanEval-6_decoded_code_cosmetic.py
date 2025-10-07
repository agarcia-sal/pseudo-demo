from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        deepest_level: int = 0
        idx: int = 0
        length: int = len(group_string)
        while idx < length:
            current_char: str = group_string[idx]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > deepest_level:
                    deepest_level = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return deepest_level

    split_groups: List[str] = []
    temp_str: str = ""
    i: int = 0
    length: int = len(parentheses_string)
    while i < length:
        c: str = parentheses_string[i]
        if c == ' ':
            if temp_str:
                split_groups.append(temp_str)
                temp_str = ""
        else:
            temp_str += c
        i += 1
    if temp_str:
        split_groups.append(temp_str)

    result_list: List[int] = []
    for single_group in split_groups:
        result_list.append(parse_paren_group(single_group))

    return result_list