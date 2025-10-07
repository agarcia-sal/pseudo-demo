from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        current_counter = 0
        max_counter = 0
        for character in group_string:
            if character == '(':
                current_counter += 1
                if current_counter > max_counter:
                    max_counter = current_counter
            else:
                current_counter -= 1
        return max_counter

    segments = parentheses_string.split(' ')
    results: List[int] = []
    for segment in segments:
        if segment != "":
            results.append(parse_paren_group(segment))
    return results