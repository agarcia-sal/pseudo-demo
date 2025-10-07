from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:

    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        peak_depth: int = 0
        iterator_index: int = 0
        length: int = len(group_string)
        while iterator_index < length:
            current_char: str = group_string[iterator_index]
            if current_char == '(':
                depth_counter += 1
                if depth_counter > peak_depth:
                    peak_depth = depth_counter
            else:
                depth_counter -= 1
            iterator_index += 1
        return peak_depth

    split_groups: List[str] = parentheses_string.split(" ")
    results_list: List[int] = []
    for candidate in split_groups:
        if candidate != "":
            depth_result: int = parse_paren_group(candidate)
            results_list.append(depth_result)
    return results_list