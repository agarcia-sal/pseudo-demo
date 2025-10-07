from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        sum_depth = 0
        top_depth = 0
        idx = 0
        while idx < len(group_string):
            sym = group_string[idx]
            if sym == '(':
                sum_depth += 1
                if sum_depth > top_depth:
                    top_depth = sum_depth
            elif sym == ')':
                sum_depth -= 1
            idx += 1
        return top_depth

    all_groups: List[str] = []
    start_pos = 0
    end_pos = 0
    length = len(parentheses_string)
    while end_pos <= length:
        if end_pos == length or parentheses_string[end_pos] == ' ':
            segment = parentheses_string[start_pos:end_pos]
            if segment:
                all_groups.append(segment)
            start_pos = end_pos + 1
        end_pos += 1

    depths: List[int] = []
    i = 0
    while i < len(all_groups):
        current_group = all_groups[i]
        depth_value = parse_paren_group(current_group)
        depths.append(depth_value)
        i += 1

    return depths