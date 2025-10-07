from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        max_level = 0
        level = 0
        for char in group_string:
            if char == '(':
                level += 1
                if level > max_level:
                    max_level = level
            else:
                level -= 1
        return max_level

    segments = [s for s in parentheses_string.split(' ') if s != '']
    depths: List[int] = []
    for segment in segments:
        depths.append(parse_paren_group(segment))
    return depths