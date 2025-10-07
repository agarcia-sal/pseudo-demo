from typing import List

def separate_paren_groups(str_param: str) -> List[str]:
    acc_results: List[str] = []
    acc_chars: List[str] = []
    depth_counter: int = 0
    idx: int = 0

    while idx < len(str_param):
        curr_char = str_param[idx]

        if curr_char == '(':
            depth_counter += 1
            acc_chars.append(curr_char)
        elif curr_char == ')':
            depth_counter -= 1
            acc_chars.append(curr_char)
            if depth_counter == 0:
                acc_results.append(''.join(acc_chars))
                acc_chars.clear()
        # Other characters are ignored explicitly per pseudocode
        idx += 1

    return acc_results