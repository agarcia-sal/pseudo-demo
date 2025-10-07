from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    groups = paren_string.split(' ')
    result_list = []
    for group in groups:
        if group:
            max_depth_of_group = parse_paren_group(group)
            result_list.append(max_depth_of_group)
    return result_list