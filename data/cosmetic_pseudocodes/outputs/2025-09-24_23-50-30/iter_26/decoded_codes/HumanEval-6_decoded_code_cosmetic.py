from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(sequence_string: str) -> int:
        depth_counter = 0
        peak_depth = 0
        for symbol in sequence_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > peak_depth:
                    peak_depth = depth_counter
            else:
                depth_counter -= 1
        return peak_depth

    segments: List[str] = []
    start_pos = 0
    length_string = len(parentheses_string)
    position = 0

    while position <= length_string:
        if position == length_string or parentheses_string[position] == ' ':
            part = parentheses_string[start_pos:position]
            if len(part) > 0:
                segments.append(part)
            start_pos = position + 1
        position += 1

    results: List[int] = [parse_paren_group(element) for element in segments]
    return results