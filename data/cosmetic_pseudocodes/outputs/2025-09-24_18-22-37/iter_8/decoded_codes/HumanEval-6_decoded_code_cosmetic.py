from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        max_reached_depth: int = 0
        index_tracker: int = 0
        length: int = len(group_string)
        while index_tracker < length:
            current_char: str = group_string[index_tracker]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > max_reached_depth:
                    max_reached_depth = depth_counter
            else:
                depth_counter -= 1
            index_tracker += 1
        return max_reached_depth

    split_groups: List[str] = parentheses_string.split(' ')
    parsed_depths: List[int] = []
    group_cursor: int = 0
    length_groups: int = len(split_groups)
    while group_cursor < length_groups:
        candidate_group: str = split_groups[group_cursor]
        if candidate_group != '':
            parsed_depths.append(parse_paren_group(candidate_group))
        group_cursor += 1
    return parsed_depths