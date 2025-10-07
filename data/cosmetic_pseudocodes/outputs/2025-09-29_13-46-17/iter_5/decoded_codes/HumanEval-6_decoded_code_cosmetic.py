from typing import Dict, List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        peak_depth: int = 0

        def scan_characters(index: int) -> int:
            if index > len(group_string):
                return peak_depth

            symbol = group_string[index - 1]

            if symbol == '(':
                nonlocal depth_counter, peak_depth
                depth_counter += 1
                if depth_counter > peak_depth:
                    peak_depth = depth_counter
            else:
                depth_counter -= 1

            return scan_characters(index + 1)

        return scan_characters(1)

    segments_map: Dict[int, str] = {}
    start_index = 1
    length_str = len(parentheses_string)

    while start_index <= length_str:
        next_space = parentheses_string.find(' ', start_index - 1)
        if next_space == -1:
            next_space = length_str
        fragment = parentheses_string[start_index - 1:next_space]
        if fragment:
            segments_map[start_index] = fragment
        start_index = next_space + 2  # move past space (index is 1-based)

    results_accumulator: List[int] = []
    for key in segments_map:
        outcome = parse_paren_group(segments_map[key])
        results_accumulator.append(outcome)

    return results_accumulator