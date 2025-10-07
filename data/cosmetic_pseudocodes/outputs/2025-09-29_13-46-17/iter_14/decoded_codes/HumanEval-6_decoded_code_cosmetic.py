from typing import List

def parse_nested_parens(parentheses_string: str) -> List:
    max_depth: int = 0
    current_depth: int = 0

    def max_nested_depth(s: str) -> int:
        nonlocal max_depth, current_depth
        max_depth = 0
        current_depth = 0
        for c in s:
            if c == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif c == ')':
                current_depth -= 1
        return max_depth

    def helper(parts: List[str]) -> List:
        result: List = []
        idx = 0
        n = len(parts)
        while idx < n:
            part = parts[idx]
            if part != '':
                result.append(parse_nested_parens(part))
            idx += 1
        return result

    parts = parentheses_string.split(' ')
    return helper(parts)