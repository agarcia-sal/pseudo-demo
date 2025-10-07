from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        deepest_level = 0
        idx = 0
        while idx < len(group_string):
            current_char = group_string[idx]
            if current_char == '(':
                temp_depth = depth_counter + 1
                depth_counter = temp_depth
                if temp_depth > deepest_level:
                    deepest_level = temp_depth
            else:
                depth_counter -= 1
            idx += 1
        return deepest_level

    split_groups: List[str] = []
    accum_str = ""
    position = 0
    while position < len(parentheses_string):
        char_at_pos = parentheses_string[position]
        if char_at_pos == ' ':
            if accum_str:
                split_groups.append(accum_str)
                accum_str = ""
        else:
            accum_str += char_at_pos
        position += 1
    if accum_str:
        split_groups.append(accum_str)

    results: List[int] = []
    iter_idx = 0
    while iter_idx < len(split_groups):
        current_group = split_groups[iter_idx]
        if current_group:
            depth_value = parse_paren_group(current_group)
            results.append(depth_value)
        iter_idx += 1

    return results