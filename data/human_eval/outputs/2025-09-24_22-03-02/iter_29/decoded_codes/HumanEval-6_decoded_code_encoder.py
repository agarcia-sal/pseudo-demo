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

    result = []
    parts = []
    start_index = 0
    for index, current_char in enumerate(paren_string):
        if current_char == ' ':
            substring = paren_string[start_index:index]
            if substring != '':
                parts.append(substring)
            start_index = index + 1
    substring = paren_string[start_index:]
    if substring != '':
        parts.append(substring)

    for x in parts:
        value = parse_paren_group(x)
        result.append(value)
    return result