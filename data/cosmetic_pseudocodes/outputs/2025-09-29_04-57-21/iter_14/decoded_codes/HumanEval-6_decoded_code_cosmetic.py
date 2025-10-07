from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        tracker_depth: int = 0
        peak_depth: int = 0
        pos: int = 0

        while pos < len(group_string):
            symbol: str = group_string[pos]
            if symbol == '(':
                tracker_depth += 1
                if peak_depth < tracker_depth:
                    peak_depth = tracker_depth
            else:
                tracker_depth -= 1
            pos += 1
        return peak_depth

    cluster_list: List[int] = []
    start_idx: int = 0
    idx: int = 0
    input_len: int = len(parentheses_string)

    while idx <= input_len:
        if idx == input_len or parentheses_string[idx] == ' ':
            segment: str = parentheses_string[start_idx:idx]
            if len(segment) > 0:
                cluster_list.append(parse_paren_group(segment))
            start_idx = idx + 1
        idx += 1

    return cluster_list