from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def depth_tracker(current_index: int, current_depth: int, max_found: int) -> int:
            if current_index > len(group_string):
                return max_found
            if group_string[current_index - 1] == '(':
                new_depth = current_depth + 1
                new_max = max(max_found, new_depth)
                return depth_tracker(current_index + 1, new_depth, new_max)
            else:
                return depth_tracker(current_index + 1, current_depth - 1, max_found)

        return depth_tracker(1, 0, 0)

    def split_groups(s: str, index: int, acc: List[str]) -> List[str]:
        if index > len(s):
            return acc
        start_idx = index
        while index <= len(s) and s[index - 1] != ' ':
            index += 1
        token = s[start_idx - 1 : index - 1]
        if token:
            acc.append(token)
        while index <= len(s) and s[index - 1] == ' ':
            index += 1
        return split_groups(s, index, acc)

    groups = split_groups(parentheses_string, 1, [])
    result: List[int] = []
    for grp in groups:
        if grp:
            result.append(parse_paren_group(grp))
    return result