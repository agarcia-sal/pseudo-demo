from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def helper(chars_list: List[str], curr_depth: int, max_depth: int) -> int:
            if not chars_list:
                return max_depth
            current_char = chars_list[0]
            rest_chars = chars_list[1:]
            updated_depth = curr_depth + 1 if current_char == '(' else curr_depth - 1
            updated_max = max(max_depth, updated_depth)
            return helper(rest_chars, updated_depth, updated_max)

        return helper(list(group_string), 0, 0)

    chunks = [chunk for chunk in parentheses_string.split(' ') if chunk != '']
    results = [parse_paren_group(x) for x in chunks]
    return results