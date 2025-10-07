from typing import List


def separate_paren_groups(input_string: str) -> List[str]:
    results: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    while idx < len(input_string):
        current_char: str = input_string[idx]

        if current_char == '(':
            depth_counter += 1
            temp_chars.append(current_char)

        else:
            if current_char == ')':
                depth_counter -= 1
                temp_chars.append(current_char)

                if depth_counter == 0:
                    group_string: str = "".join(temp_chars)
                    results.append(group_string)
                    temp_chars.clear()
        idx += 1

    return results