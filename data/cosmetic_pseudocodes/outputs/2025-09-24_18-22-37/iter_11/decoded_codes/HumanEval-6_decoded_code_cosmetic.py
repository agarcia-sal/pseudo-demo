from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        highest_depth = 0
        idx = 0
        len_group = len(group_string)

        while idx < len_group:
            current_char = group_string[idx]

            if current_char == '(':
                depth_counter += 1
                if depth_counter > highest_depth:
                    highest_depth = depth_counter
            else:
                depth_counter -= 1
            idx += 1

        return highest_depth

    all_groups: List[str] = []
    start_idx = 0
    str_len = len(parentheses_string)
    end_idx = 0

    while end_idx < str_len:
        if parentheses_string[end_idx] == ' ':
            temp_group = parentheses_string[start_idx:end_idx]
            if temp_group:
                all_groups.append(temp_group)
            start_idx = end_idx + 1
        end_idx += 1

    last_group = parentheses_string[start_idx:str_len]
    if last_group:
        all_groups.append(last_group)

    result_list: List[int] = []
    group_pos = 0
    groups_len = len(all_groups)

    while group_pos < groups_len:
        current_group = all_groups[group_pos]
        depth_val = parse_paren_group(current_group)
        result_list.append(depth_val)
        group_pos += 1

    return result_list