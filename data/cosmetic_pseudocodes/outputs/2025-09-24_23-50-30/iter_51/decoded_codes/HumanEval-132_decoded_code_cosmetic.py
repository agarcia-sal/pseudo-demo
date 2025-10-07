from typing import List

def is_nested(str_arg: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    def recur_index_capture(curr_idx: int) -> None:
        if curr_idx == len(str_arg) - 1:
            if str_arg[curr_idx] == '[':
                open_positions.append(curr_idx)
            else:
                close_positions.append(curr_idx)
        else:
            if str_arg[curr_idx] == '[':
                open_positions.append(curr_idx)
            else:
                close_positions.append(curr_idx)
            recur_index_capture(curr_idx + 1)

    recur_index_capture(0)

    close_positions.reverse()

    match_counter = 0
    current_pos = 0
    max_pos = len(close_positions)

    def evaluate_matches(index_list: List[int]) -> None:
        nonlocal match_counter, current_pos
        if not index_list:
            return
        head_val = index_list[0]
        tail_list = index_list[1:]

        if (current_pos < max_pos) and (head_val < close_positions[current_pos]):
            match_counter += 1
            current_pos += 1

        evaluate_matches(tail_list)

    evaluate_matches(open_positions)

    return match_counter >= 2