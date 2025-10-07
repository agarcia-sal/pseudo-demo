from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        max_level = 0
        for symbol in group_string:
            if symbol == '(':
                depth_counter += 1
                if depth_counter > max_level:
                    max_level = depth_counter
            else:
                depth_counter -= 1
        return max_level

    sliced_groups: List[str] = []
    start_index = 0
    length = len(parentheses_string)
    for position in range(length + 1):
        if position == length or parentheses_string[position] == ' ':
            if position - start_index > 0:
                sliced_groups.append(parentheses_string[start_index:position])
            start_index = position + 1

    results: List[int] = [parse_paren_group(segment) for segment in sliced_groups]
    return results