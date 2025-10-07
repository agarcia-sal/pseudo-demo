from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter = 0
        highest_depth = 0
        index = 0
        while index < len(group_string):
            symbol = group_string[index]
            if symbol != '(':
                depth_counter -= 1
            else:
                depth_counter += 1
                if highest_depth < depth_counter:
                    highest_depth = depth_counter
            index += 1
        return highest_depth

    segments: List[str] = []
    cursor = 0
    length_str = len(parentheses_string)
    while cursor < length_str:
        start_pos = cursor
        while cursor < length_str and parentheses_string[cursor] != ' ':
            cursor += 1
        candidate_segment = parentheses_string[start_pos:cursor]
        if candidate_segment:
            segments.append(candidate_segment)
        cursor += 1  # Skip the space or move past end

    result_list: List[int] = []
    iter_index = 0
    while iter_index < len(segments):
        result_list.append(parse_paren_group(segments[iter_index]))
        iter_index += 1

    return result_list