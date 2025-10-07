from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        idx: int = 0
        depth_tracker: int = 0
        max_depth_record: int = 0

        while idx < len(group_string):
            char = group_string[idx]
            if char == '(':
                depth_tracker += 1
                if depth_tracker > max_depth_record:
                    max_depth_record = depth_tracker
            elif char == ')':
                depth_tracker -= 1
            idx += 1
        return max_depth_record

    segments: List[str] = []
    temp_str: str = ""
    char_pos: int = 0

    while char_pos < len(parentheses_string):
        char = parentheses_string[char_pos]
        if char == ' ':
            if temp_str:
                segments.append(temp_str)
                temp_str = ""
        else:
            temp_str += char
        char_pos += 1

    if temp_str:
        segments.append(temp_str)

    result_list: List[int] = []
    i: int = 0
    while i < len(segments):
        if segments[i]:
            result_list.append(parse_paren_group(segments[i]))
        i += 1

    return result_list