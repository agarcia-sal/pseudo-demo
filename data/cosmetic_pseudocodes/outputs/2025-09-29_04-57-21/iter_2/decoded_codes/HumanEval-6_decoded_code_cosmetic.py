from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_chars: str) -> int:
        max_depth_val: int = 0
        nesting_level: int = 0
        idx: int = 0
        length: int = len(group_chars)
        while idx < length:
            char_symbol: str = group_chars[idx]
            if char_symbol == '(':
                nesting_level += 1
                if nesting_level > max_depth_val:
                    max_depth_val = nesting_level
            else:
                nesting_level -= 1
            idx += 1
        return max_depth_val

    sequence_groups: List[str] = []
    start_index: int = 0
    length: int = len(parentheses_string)
    for i in range(length + 1):
        if i == length or parentheses_string[i] == ' ':
            segment = parentheses_string[start_index:i]
            if segment != "":
                sequence_groups.append(segment)
            start_index = i + 1

    depth_results: List[int] = [parse_paren_group(group_str) for group_str in sequence_groups]
    return depth_results