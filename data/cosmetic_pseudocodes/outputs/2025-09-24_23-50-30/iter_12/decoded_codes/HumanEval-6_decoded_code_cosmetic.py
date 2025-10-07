from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_str: str) -> int:
        def depth_helper(index: int, curr_depth: int, max_depth: int) -> int:
            if index == len(group_str):
                return max_depth
            char = group_str[index]
            if char == '(':
                ascended_depth = curr_depth + 1
                updated_max = max(ascended_depth, max_depth)
                return depth_helper(index + 1, ascended_depth, updated_max)
            else:
                return depth_helper(index + 1, curr_depth - 1, max_depth)
        return depth_helper(0, 0, 0)

    segments = [segment for segment in parentheses_string.split() if segment != ""]
    depths = [parse_paren_group(segment) for segment in segments]
    return depths