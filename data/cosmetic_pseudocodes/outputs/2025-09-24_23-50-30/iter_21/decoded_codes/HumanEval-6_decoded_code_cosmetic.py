from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_current: int = 0
        depth_maximum: int = 0
        idx: int = 0
        length_group: int = len(group_string)

        while idx < length_group:
            ch: str = group_string[idx]
            if ch == '(':
                depth_current += 1
                if depth_current > depth_maximum:
                    depth_maximum = depth_current
            elif ch == ')':
                depth_current -= 1
            idx += 1

        return depth_maximum

    output_list: List[int] = []
    temp_index: int = 0
    input_length: int = len(parentheses_string)
    word_buffer: str = ''

    while temp_index <= input_length:
        if temp_index == input_length or parentheses_string[temp_index] == ' ':
            if len(word_buffer) > 0:
                output_list.append(parse_paren_group(word_buffer))
                word_buffer = ''
        else:
            word_buffer += parentheses_string[temp_index]
        temp_index += 1

    return output_list