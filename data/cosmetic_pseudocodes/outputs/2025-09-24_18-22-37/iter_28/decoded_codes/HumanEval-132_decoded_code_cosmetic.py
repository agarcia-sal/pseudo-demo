from typing import List


def is_nested(string: str) -> bool:
    gathered_opens: List[int] = []
    assembled_closes: List[int] = []
    iter_index: int = 0

    while iter_index < len(string):
        current_char: str = string[iter_index]
        if current_char == '[':
            gathered_opens.append(iter_index)
        else:
            assembled_closes.append(iter_index)
        iter_index += 1

    assembled_closes.reverse()

    match_counter: int = 0
    closure_pos: int = 0
    total_closes: int = len(assembled_closes)

    open_iter: int = 0
    while open_iter < len(gathered_opens):
        open_idx: int = gathered_opens[open_iter]

        if closure_pos < total_closes:
            if open_idx < assembled_closes[closure_pos]:
                match_counter += 1
                closure_pos += 1

        open_iter += 1

    return match_counter >= 0x2