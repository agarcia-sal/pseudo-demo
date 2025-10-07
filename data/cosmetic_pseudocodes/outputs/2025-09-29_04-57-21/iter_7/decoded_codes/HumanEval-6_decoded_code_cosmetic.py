from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_reached = 0
        idx = 0
        while idx < len(group_string):
            ch = group_string[idx]
            if ch == '(':
                depth_counter += 1
                if depth_counter > max_reached:
                    max_reached = depth_counter
            else:
                depth_counter -= 1
            idx += 1
        return max_reached

    segments = [token for token in parentheses_string.split(' ') if token != '']

    results: List[int] = []
    i = 0
    while i < len(segments):
        results.append(parse_paren_group(segments[i]))
        i += 1
    return results