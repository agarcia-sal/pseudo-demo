from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_tracker: int = 0
        max_tracker: int = 0
        for symbol in group_string:
            if symbol == '(':
                depth_tracker += 1
                if depth_tracker > max_tracker:
                    max_tracker = depth_tracker
            else:
                depth_tracker -= 1
        return max_tracker

    segment_list: List[str] = []
    start_idx: int = 0
    current_idx: int = 0
    length: int = len(parentheses_string)
    while current_idx <= length:
        if current_idx == length or parentheses_string[current_idx] == ' ':
            segment_length: int = current_idx - start_idx
            if segment_length > 0:
                segment_list.append(parentheses_string[start_idx:current_idx])
            start_idx = current_idx + 1
        current_idx += 1

    result_list: List[int] = []
    for element in segment_list:
        if element != "":
            result_list.append(parse_paren_group(element))

    return result_list