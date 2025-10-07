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
    current_part = ""
    for character in paren_string:
        if character == ' ':
            if current_part != "":
                parts.append(current_part)
                current_part = ""
        else:
            current_part += character
    if current_part != "":
        parts.append(current_part)

    for part in parts:
        result.append(parse_paren_group(part))

    return result