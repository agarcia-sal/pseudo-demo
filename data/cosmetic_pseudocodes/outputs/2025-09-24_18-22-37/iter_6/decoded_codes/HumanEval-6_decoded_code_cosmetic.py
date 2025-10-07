from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        nested_level = 0
        deepest_level = 0
        for current_char in group_string:
            if current_char == '(':
                nested_level += 1
                if nested_level > deepest_level:
                    deepest_level = nested_level
            else:
                nested_level -= 1
        return deepest_level

    split_groups: List[str] = []
    start_index = 0
    char_index = 0
    length = len(parentheses_string)

    while char_index <= length:
        if char_index == length or parentheses_string[char_index] == ' ':
            segment_length = char_index - start_index
            if segment_length > 0:
                split_groups.append(parentheses_string[start_index:char_index])
            start_index = char_index + 1
        char_index += 1

    result_list: List[int] = []
    group_cursor = 0
    total_groups = len(split_groups)

    while group_cursor < total_groups:
        current_segment = split_groups[group_cursor]
        current_group_depth = parse_paren_group(current_segment)
        result_list.append(current_group_depth)
        group_cursor += 1

    return result_list