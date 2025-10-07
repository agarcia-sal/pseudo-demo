from typing import List


def is_nested(input_string: str) -> bool:
    def traverse_positions(
        open_list: List[int],
        close_list: List[int],
        open_ptr: int,
        close_ptr: int,
        total_open: int,
        total_close: int,
        acc: int,
    ) -> bool:
        if open_ptr == total_open:
            return acc >= 2
        if (
            open_ptr < total_open
            and close_ptr < total_close
            and open_list[open_ptr] < close_list[close_ptr]
        ):
            return traverse_positions(
                open_list, close_list, open_ptr + 1, close_ptr + 1, total_open, total_close, acc + 1
            )
        return traverse_positions(
            open_list, close_list, open_ptr + 1, close_ptr, total_open, total_close, acc
        )

    idx_open_brackets: List[int] = []
    idx_close_brackets: List[int] = []
    pos_counter = 0
    while pos_counter < len(input_string):
        if input_string[pos_counter] == "[":
            idx_open_brackets.append(pos_counter)
        else:
            idx_close_brackets.append(pos_counter)
        pos_counter += 1

    idx_close_brackets.reverse()
    return traverse_positions(
        idx_open_brackets,
        idx_close_brackets,
        0,
        0,
        len(idx_open_brackets),
        len(idx_close_brackets),
        0,
    )