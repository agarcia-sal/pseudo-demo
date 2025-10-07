from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    group_collection: List[str] = []
    index: int = 0
    length_string: int = len(parentheses_string)
    while index < length_string:
        start_pos: int = index
        while index < length_string and parentheses_string[index] != ' ':
            index += 1
        if start_pos < index:
            group_collection.append(parentheses_string[start_pos:index])
        index += 1

    result_collection: List[int] = []
    for current_group in group_collection:
        depth_current: int = 0
        max_depth_recorded: int = 0
        pos_in_group: int = 0
        while pos_in_group < len(current_group):
            char_current: str = current_group[pos_in_group]
            if char_current != '(':
                depth_current -= 1
                pos_in_group += 1
                continue
            depth_current += 1
            if max_depth_recorded < depth_current:
                max_depth_recorded = depth_current
            pos_in_group += 1
        result_collection.append(max_depth_recorded)

    return result_collection