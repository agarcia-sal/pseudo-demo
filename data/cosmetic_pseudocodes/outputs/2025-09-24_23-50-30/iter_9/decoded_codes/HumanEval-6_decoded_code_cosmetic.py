from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        peak_depth: int = 0
        idx: int = 0
        while idx < len(group_string):
            char = group_string[idx]
            if char == '(':
                depth_counter += 1
                if peak_depth < depth_counter:
                    peak_depth = depth_counter
            elif char == ')':
                depth_counter -= 1
            idx += 1
        return peak_depth

    chunked_groups: List[str] = []
    start_idx: int = 0
    length: int = len(parentheses_string)
    for pos in range(length + 1):
        if pos == length or parentheses_string[pos] == ' ':
            if pos > 0 and parentheses_string[pos - 1] != ' ':
                chunked_groups.append(parentheses_string[start_idx:pos])
            start_idx = pos + 1

    results: List[int] = []
    for entry in chunked_groups:
        if len(entry) > 0:
            results.append(parse_paren_group(entry))
    return results