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

    tokens = []
    start_index = 0
    length = len(paren_string)

    for i in range(length):
        if paren_string[i] == ' ':
            if start_index < i:
                tokens.append(paren_string[start_index:i])
            start_index = i + 1

    if start_index < length:
        tokens.append(paren_string[start_index:length])

    result = [parse_paren_group(token) for token in tokens]
    return result