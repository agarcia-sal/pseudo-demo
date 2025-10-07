from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        tracker_depth: int = 0
        peak_depth: int = 0
        pointer_index: int = 0
        length: int = len(group_string)
        while pointer_index < length:
            current_char: str = group_string[pointer_index]
            if current_char == '(':
                tracker_depth += 1
                if tracker_depth > peak_depth:
                    peak_depth = tracker_depth
            elif current_char == ')':
                tracker_depth -= 1
            pointer_index += 1
        return peak_depth

    fragment_list: List[str] = parentheses_string.split(' ')
    results: List[int] = []
    iterator_position: int = 0
    length: int = len(fragment_list)
    while iterator_position < length:
        candidate: str = fragment_list[iterator_position]
        if candidate != '':
            results.append(parse_paren_group(candidate))
        iterator_position += 1
    return results