from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_level = 0
        for symbol in group_string:
            if symbol != '(':
                depth_counter -= 1
            else:
                depth_counter += 1
                if depth_counter > max_level:
                    max_level = depth_counter
        return max_level

    segments: List[str] = []
    temp = ""
    idx = 0
    length = len(parentheses_string)
    while idx <= length:
        if idx == length or parentheses_string[idx] == ' ':
            if temp:
                segments.append(temp)
                temp = ""
        else:
            temp += parentheses_string[idx]
        idx += 1

    result: List[int] = []
    for segment in segments:
        result.append(parse_paren_group(segment))
    return result