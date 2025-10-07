from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(inspect_string: str) -> int:
        depth_counter = 0
        peak_depth = 0
        for current_char in inspect_string:
            if current_char == '(':
                depth_counter += 1
                if depth_counter > peak_depth:
                    peak_depth = depth_counter
            else:
                depth_counter -= 1
        return peak_depth

    fragmented_list = parentheses_string.split(' ')
    results_collection: List[int] = []
    for candidate_str in fragmented_list:
        if candidate_str != '':
            results_collection.append(parse_paren_group(candidate_str))
    return results_collection