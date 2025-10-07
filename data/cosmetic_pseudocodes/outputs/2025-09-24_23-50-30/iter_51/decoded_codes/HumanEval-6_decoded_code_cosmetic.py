from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(substring: str) -> int:
        def iter_chars(index: int, depth_curr: int, depth_max: int) -> int:
            if index >= len(substring):
                return depth_max
            if substring[index] == '(':
                new_depth = depth_curr + 1
                return iter_chars(index + 1, new_depth, max(new_depth, depth_max))
            else:
                # assuming only '(' and ')' characters as per context
                return iter_chars(index + 1, depth_curr - 1, depth_max)

        return iter_chars(1, 0, 0)

    token_list: List[str] = []
    pos = 0
    len_str = len(parentheses_string)

    def collect_tokens() -> None:
        nonlocal pos
        if pos >= len_str:
            return
        start_idx = pos
        while pos < len_str and parentheses_string[pos] != ' ':
            pos += 1
        if start_idx < pos:
            token_list.append(parentheses_string[start_idx:pos])
        while pos < len_str and parentheses_string[pos] == ' ':
            pos += 1
        collect_tokens()

    while pos < len_str and parentheses_string[pos] == ' ':
        pos += 1
    collect_tokens()
    return [parse_paren_group(g) for g in token_list if len(g) > 0]