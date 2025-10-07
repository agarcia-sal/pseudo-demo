from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        max_depth_value: int = 0
        index: int = 0
        length: int = len(group_string)
        while index < length:
            current_char: str = group_string[index]
            if current_char == '(':
                depth_counter += 1
                if max_depth_value < depth_counter:
                    max_depth_value = depth_counter
            else:
                depth_counter -= 1
            index += 1
        return max_depth_value

    split_groups: List[str] = []
    start_pos: int = 0
    length: int = len(parentheses_string)
    for position in range(length + 1):
        if position == length or parentheses_string[position] == ' ':
            segment: str = parentheses_string[start_pos:position]
            if segment != "":
                split_groups.append(segment)
            start_pos = position + 1

    depths_list: List[int] = []
    for each_group in split_groups:
        depths_list.append(parse_paren_group(each_group))

    return depths_list