from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        deepest_level = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > deepest_level:
                    deepest_level = depth_counter
            else:
                depth_counter -= 1
        return deepest_level

    segment_list = parentheses_string.split()
    results: List[int] = []
    for segment in segment_list:
        if len(segment) > 0:
            results.append(parse_paren_group(segment))
    return results