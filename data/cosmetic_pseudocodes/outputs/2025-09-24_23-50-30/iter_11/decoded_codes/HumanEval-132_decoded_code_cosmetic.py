from typing import List


def is_nested(str_input: str) -> bool:
    open_stack: List[int] = []
    close_stack: List[int] = []
    pos_counter: int = 0
    str_len: int = len(str_input)

    for idx in range(str_len):
        if str_input[idx] != '[':
            close_stack.append(idx)
        else:
            open_stack.append(idx)

    close_stack.reverse()

    cmp_idx: int = 0
    total_pairs: int = 0
    p_limit: int = len(close_stack)

    while cmp_idx < p_limit and pos_counter < len(open_stack):
        chosen_open = open_stack[pos_counter]
        chosen_close = close_stack[cmp_idx]

        if chosen_open < chosen_close:
            total_pairs += 1
            pos_counter += 1

        cmp_idx += 1

    return total_pairs >= 2