from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        highest_level: int = 0
        idx: int = 0
        while idx < len(group_string):
            ch = group_string[idx]
            if ch == '(':
                depth_counter += 1
                if depth_counter > highest_level:
                    highest_level = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return highest_level

    segments: List[str] = []
    buffer: str = ""
    pos: int = 0
    length: int = len(parentheses_string)
    while pos <= length:
        if pos == length or parentheses_string[pos] == ' ':
            if buffer:
                segments.append(buffer)
                buffer = ""
        else:
            buffer += parentheses_string[pos]
        pos += 1

    results: List[int] = []
    i: int = 0
    while i < len(segments):
        segment = segments[i]
        if segment:
            results.append(parse_paren_group(segment))
        i += 1

    return results