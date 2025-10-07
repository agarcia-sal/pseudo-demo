from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def helper(index: int, depth: int, max_depth: int) -> int:
            if index >= len(group_string):
                return max_depth
            if group_string[index] == '(':
                next_depth = depth + 1
                return helper(index + 1, next_depth, max(next_depth, max_depth))
            else:
                return helper(index + 1, depth - 1, max_depth)

        return helper(0, 0, 0)

    result: List[int] = []
    tokens: List[str] = []
    temp_string: str = ""
    for ch in parentheses_string:
        if ch == ' ':
            if temp_string:
                tokens.append(temp_string)
                temp_string = ""
        else:
            temp_string += ch
    if temp_string:
        tokens.append(temp_string)

    for token in tokens:
        result.append(parse_paren_group(token))
    return result