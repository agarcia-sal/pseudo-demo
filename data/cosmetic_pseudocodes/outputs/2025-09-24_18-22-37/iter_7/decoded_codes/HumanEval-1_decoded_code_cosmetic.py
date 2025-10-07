from typing import List


def separate_paren_groups(parens_string: str) -> List[str]:
    results_list: List[str] = []
    temp_string_list: List[str] = []
    depth_counter: int = 0

    index: int = 0
    length: int = len(parens_string)
    while index < length:
        current_char: str = parens_string[index]

        if current_char == '(':
            depth_counter += 1
            temp_string_list.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            temp_string_list.append(current_char)
            if depth_counter == 0:
                # Concatenate collected characters
                concatenated_string = ''.join(temp_string_list)
                results_list.append(concatenated_string)
                temp_string_list.clear()
        else:
            # no action for other characters
            pass

        index += 1

    return results_list