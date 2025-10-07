from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        max_recorded_depth: int = 0
        position: int = 0
        length: int = len(group_string)
        while position < length:
            current_char: str = group_string[position]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > max_recorded_depth:
                    max_recorded_depth = depth_counter
            else:
                depth_counter -= 1
            position += 1
        return max_recorded_depth

    raw_groups: List[str] = parentheses_string.split(" ")
    processed_results: List[int] = []
    index_var: int = 0
    length: int = len(raw_groups)
    while index_var < length:
        present_group: str = raw_groups[index_var]
        if present_group != "":
            processed_results.append(parse_paren_group(present_group))
        index_var += 1
    return processed_results