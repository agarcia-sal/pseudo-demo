from typing import List


def parse_nested_parens(input_string: str) -> List[int]:
    def parse_paren_group(substring: str) -> int:
        depth_counter = 0
        max_depth_reached = 0
        for symbol in substring:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_depth_reached:
                    max_depth_reached = depth_counter
            elif symbol == ')':
                depth_counter -= 1
        return max_depth_reached

    split_groups: List[str] = []
    start_pos = 0
    length = len(input_string)
    for idx in range(length + 1):
        if idx == length or input_string[idx] == ' ':
            if start_pos < idx:
                split_groups.append(input_string[start_pos:idx])
            start_pos = idx + 1

    result_list: List[int] = []
    pos = 0
    while pos < len(split_groups):
        if split_groups[pos] != '':
            result_list.append(parse_paren_group(split_groups[pos]))
        pos += 1

    return result_list