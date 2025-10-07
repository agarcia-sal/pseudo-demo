from typing import List


def separate_paren_groups(input_parens: str) -> List[str]:
    output_groups: List[str] = []
    temp_buffer: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    while idx < len(input_parens):
        current_char: str = input_parens[idx]

        if current_char == '(':
            depth_counter += 1
            temp_buffer.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            temp_buffer.append(current_char)

            if depth_counter == 0:
                built_string = ''.join(temp_buffer)
                output_groups.append(built_string)
                temp_buffer = []
        idx += 1

    return output_groups