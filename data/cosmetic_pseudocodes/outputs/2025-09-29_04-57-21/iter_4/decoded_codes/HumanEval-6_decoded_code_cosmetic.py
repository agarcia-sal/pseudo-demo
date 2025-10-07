from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_level = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_level:
                    max_level = depth_counter
            else:
                depth_counter -= 1
        return max_level

    segments: List[str] = []
    current_segment = ""
    for ch in parentheses_string:
        if ch == ' ':
            if current_segment:
                segments.append(current_segment)
                current_segment = ""
        else:
            current_segment += ch
    if current_segment:
        segments.append(current_segment)

    results: List[int] = []
    for part in segments:
        results.append(parse_paren_group(part))

    return results