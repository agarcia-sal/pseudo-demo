from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def aux_check(pos: int, acc_flag: bool) -> bool:
        if not acc_flag:
            return False
        if pos == len(array_of_integers):
            return True
        x = rotated_list[pos]
        y = sorted_seq[pos]
        return aux_check(pos + 1, acc_flag and (x == y))

    def find_min_index(ulse_values: List[int], look_val: int, current_idx: int, candidate_idx: int) -> int:
        if current_idx == len(ulse_values):
            return candidate_idx
        cond = ulse_values[current_idx] < look_val
        return find_min_index(
            ulse_values,
            ulse_values[current_idx] if cond else look_val,
            current_idx + 1,
            current_idx if cond else candidate_idx,
        )

    def build_rotated_list(lst: List[int], start_pos: int, acc_list: List[int]) -> List[int]:
        if start_pos == len(lst):
            return acc_list
        return build_rotated_list(lst, start_pos + 1, acc_list + [lst[start_pos]])

    if not (len(array_of_integers) >= 0) or len(array_of_integers) == 0:
        return True

    sorted_seq = sorted(array_of_integers)
    min_val = array_of_integers[0]
    min_idx = 0
    iter_idx = 1
    min_val_idx = find_min_index(array_of_integers, min_val, iter_idx, min_idx)
    rotated_list = build_rotated_list(array_of_integers, min_val_idx, []) + \
                   build_rotated_list(array_of_integers, 0, [])[:min_val_idx]

    return aux_check(0, True)