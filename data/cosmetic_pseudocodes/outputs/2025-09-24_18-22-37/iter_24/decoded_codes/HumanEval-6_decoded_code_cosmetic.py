from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        highest_depth = 0
        idx = 0
        length = len(group_string)
        while idx < length:
            ch = group_string[idx]
            if ch == '(':
                depth_counter += 1
                if depth_counter > highest_depth:
                    highest_depth = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return highest_depth

    split_groups: List[str] = []
    temp_str = ""
    i = 0
    total_len = len(parentheses_string)
    while i < total_len:
        current_char = parentheses_string[i]
        if current_char == ' ':
            if temp_str:
                split_groups.append(temp_str)
                temp_str = ""
        else:
            temp_str += current_char
        i += 1
    if temp_str:
        split_groups.append(temp_str)

    result_collection: List[int] = []
    for group_element in split_groups:
        if group_element != "":
            result_collection.append(parse_paren_group(group_element))

    return result_collection