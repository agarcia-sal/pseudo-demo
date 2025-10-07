from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth: int = 0
        max_depth: int = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif c == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError("Unbalanced parentheses: too many closing parens")
            else:
                raise ValueError(f"Invalid character in input: {c}")
        if depth != 0:
            raise ValueError("Unbalanced parentheses: mismatched opening and closing parens")
        return max_depth

    if not isinstance(paren_string, str):
        raise ValueError("Input must be a string")

    groups: List[str] = paren_string.split(' ')
    result_list: List[int] = []
    for group in groups:
        if group:
            result_list.append(parse_paren_group(group))
    return result_list