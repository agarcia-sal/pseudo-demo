from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def recurse(index: int, cur_depth: int, max_depth: int) -> int:
            if index == len(group_string):
                return max_depth
            char = group_string[index]
            new_cur_depth = cur_depth + (1 if char == '(' else -1)
            new_max_depth = max(max_depth, new_cur_depth)
            return recurse(index + 1, new_cur_depth, new_max_depth)
        return recurse(0, 0, 0)

    non_empty_groups = [x for x in parentheses_string.split(' ') if len(x) > 0]
    result: List[int] = []
    index = 0
    while index < len(non_empty_groups):
        result.append(parse_paren_group(non_empty_groups[index]))
        index += 1
    return result