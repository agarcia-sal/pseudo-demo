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

    result: List[int] = []
    parts: List[str] = []
    current_string = ''
    for char in paren_string:
        if char == ' ':
            if current_string != '':
                parts.append(current_string)
                current_string = ''
        else:
            current_string += char
    if current_string != '':
        parts.append(current_string)

    for x in parts:
        result.append(parse_paren_group(x))

    return result