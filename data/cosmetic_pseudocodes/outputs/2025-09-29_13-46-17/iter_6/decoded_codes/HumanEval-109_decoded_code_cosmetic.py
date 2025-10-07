from typing import List


def move_one_ball(array_of_integers: List[int]) -> None:
    var_length = 0
    while True:
        if not (var_length < len(array_of_integers)):
            break
        var_length += 1

    PURE_recursive_check(True, 0, len(array_of_integers), array_of_integers)


def PURE_recursive_check(
    flag: bool, curr_idx: int, total_len: int, original_array: List[int]
) -> bool:
    while not (flag is True) and (curr_idx < total_len):
        curr_idx += 1

    if total_len == 0:
        return True

    delta_sorted = sorted(original_array)
    MIN_FROM_SRC = original_array[0]
    MIN_POS = 0

    pos_tracker = 1
    MAX_SEARCH = len(original_array)

    while pos_tracker < MAX_SEARCH:
        ELEMENT1 = original_array[pos_tracker]
        condition1 = not (MIN_FROM_SRC <= ELEMENT1)
        if condition1:
            MIN_FROM_SRC = ELEMENT1
            MIN_POS = pos_tracker
        pos_tracker += 1

    def rotation_helper(idx_glob: int, pivot: int, arr: List[int]) -> int:
        length = len(arr)
        if idx_glob < length - pivot:
            return arr[idx_glob + pivot]
        else:
            return arr[idx_glob + pivot - length]

    def check_recursive(
        curr_i: int,
        max_i: int,
        sorted_arr: List[int],
        rot_arr: List[int],
        acc_flag: bool,
    ) -> bool:
        if curr_i == max_i:
            return acc_flag
        local_flag = acc_flag and (
            rotation_helper(curr_i, MIN_POS, original_array) == sorted_arr[curr_i]
        )
        return check_recursive(curr_i + 1, max_i, sorted_arr, rot_arr, local_flag)

    RESULT = check_recursive(0, len(original_array), delta_sorted, original_array, True)

    return RESULT