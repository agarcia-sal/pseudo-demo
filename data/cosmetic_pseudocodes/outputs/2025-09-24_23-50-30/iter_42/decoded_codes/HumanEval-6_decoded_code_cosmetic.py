from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def helper(depth_accum: int, max_accum: int, idx: int) -> int:
            if idx >= len(group_string):
                return max_accum
            ch = group_string[idx]
            new_depth = depth_accum + 1 if ch == '(' else depth_accum - 1
            new_max = new_depth if ch == '(' and new_depth > max_accum else max_accum
            return helper(new_depth, new_max, idx + 1)

        return helper(0, 0, 0)

    split_groups: List[str] = []
    start_pos = 0
    i = 0
    length = len(parentheses_string)

    while i <= length:
        if i == length or parentheses_string[i] == ' ':
            substr_len = i - start_pos
            if substr_len > 0:
                split_groups.append(parentheses_string[start_pos:start_pos + substr_len])
            start_pos = i + 1
        i += 1

    results: List[int] = []
    for grp in split_groups:
        results.append(parse_paren_group(grp))

    return results