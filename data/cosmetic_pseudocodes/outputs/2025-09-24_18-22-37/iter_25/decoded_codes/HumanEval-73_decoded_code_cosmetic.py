from typing import List

def smallest_change(integer_list: List[int]) -> int:
    mismatch_count: int = 0
    end_index: int = len(integer_list) // 2
    front_pointer: int = 0

    while front_pointer < end_index:
        left_value: int = integer_list[front_pointer]
        right_value: int = integer_list[len(integer_list) - front_pointer - 1]
        if left_value != right_value:
            mismatch_count += 1
        front_pointer += 1

    return mismatch_count