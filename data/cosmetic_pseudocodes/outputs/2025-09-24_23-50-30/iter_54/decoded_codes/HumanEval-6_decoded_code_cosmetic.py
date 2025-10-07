from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def loop_over_chars(index: int, current_depth: int, maximum_depth: int) -> int:
            if index >= len(group_string):
                return maximum_depth
            char = group_string[index]
            updated_depth = current_depth + 1 if char == '(' else current_depth - 1
            updated_maximum = updated_depth if updated_depth > maximum_depth else maximum_depth
            return loop_over_chars(index + 1, updated_depth, updated_maximum)

        return loop_over_chars(0, 0, 0)

    all_groups: List[str] = []
    start = 0
    length_str = len(parentheses_string)

    for idx in range(length_str + 1):
        if idx == length_str or parentheses_string[idx] == ' ':
            substring = parentheses_string[start:idx]
            if substring:
                all_groups.append(substring)
            start = idx + 1

    results: List[int] = []
    for element in all_groups:
        results.append(parse_paren_group(element))

    return results