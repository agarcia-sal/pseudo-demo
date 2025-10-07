from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        current_depth = 0
        max_depth = 0
        index = 0
        length = len(group_string)
        while index < length:
            char = group_string[index]
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            else:
                current_depth -= 1
            index += 1
        return max_depth

    pieces = parentheses_string.split(' ')
    depths: List[int] = []
    for item in pieces:
        if item != '':
            depths.append(parse_paren_group(item))
    return depths