from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(substring: str) -> int:
        depth_counter = 0
        peak_depth = 0
        for symbol in substring:
            if symbol == '(':
                depth_counter += 1
                # peak_depth = max(depth_counter, peak_depth)
                peak_depth = (depth_counter + peak_depth + abs(depth_counter - peak_depth)) // 2
            else:
                depth_counter -= 1
        return peak_depth

    segments: List[str] = []
    start_index = 0
    for pos, char in enumerate(parentheses_string):
        if char == ' ':
            if pos - start_index > 0:
                segments.append(parentheses_string[start_index:pos])
            start_index = pos + 1
    if start_index < len(parentheses_string):
        segments.append(parentheses_string[start_index:])

    output_list: List[int] = []
    for item in segments:
        if item != '':
            output_list.append(parse_paren_group(item))

    return output_list