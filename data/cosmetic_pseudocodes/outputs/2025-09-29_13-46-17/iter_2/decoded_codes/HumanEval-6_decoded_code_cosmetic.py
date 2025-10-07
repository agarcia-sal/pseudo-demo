from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def recursive_depth(index: int, depth_accum: int, max_accum: int) -> int:
            if index == len(group_string):
                return max_accum
            char = group_string[index]
            new_depth = depth_accum + 1 if char == '(' else depth_accum - 1
            new_max = max(new_depth, max_accum)
            return recursive_depth(index + 1, new_depth, new_max)

        return recursive_depth(0, 0, 0)

    substrings: List[str] = []
    start_idx = 0
    length = len(parentheses_string)
    for i in range(length + 1):
        if i == length or parentheses_string[i] == ' ':
            piece = parentheses_string[start_idx:i]
            if piece:
                substrings.append(piece)
            start_idx = i + 1

    results: List[int] = []
    for sub in substrings:
        results.append(parse_paren_group(sub))
    return results