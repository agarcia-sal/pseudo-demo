from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(param_string: str) -> int:
        depth_counter = 0
        max_level = 0
        index_pos = 0
        length = len(param_string)
        while index_pos < length:
            if param_string[index_pos] == '(':
                depth_counter += 1
                if depth_counter > max_level:
                    max_level = depth_counter
            else:
                depth_counter -= 1
            index_pos += 1
        return max_level

    split_groups: List[str] = []
    start_idx = 0
    length = len(parentheses_string)
    while True:
        space_idx = parentheses_string.find(' ', start_idx)
        if space_idx == -1:
            split_groups.append(parentheses_string[start_idx:])
            break
        split_groups.append(parentheses_string[start_idx:space_idx])
        start_idx = space_idx + 1

    result_list: List[int] = []
    for item in split_groups:
        if len(item) != 0:
            result_list.append(parse_paren_group(item))

    return result_list