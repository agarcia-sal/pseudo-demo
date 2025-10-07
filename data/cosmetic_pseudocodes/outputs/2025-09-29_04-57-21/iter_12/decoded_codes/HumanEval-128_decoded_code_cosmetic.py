from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if not array_of_integers:
        return None

    sign_accumulator: int = 1

    index_pointer: int = 0
    found_zero_flag: bool = False
    while index_pointer < len(array_of_integers) and not found_zero_flag:
        current_item = array_of_integers[index_pointer]
        if current_item == 0:
            found_zero_flag = True
        index_pointer += 1

    if found_zero_flag:
        sign_accumulator = 0
    else:
        neg_count = 0
        pos_index = 0
        while pos_index < len(array_of_integers):
            element = array_of_integers[pos_index]
            if element < 0:
                neg_count += 1
            pos_index += 1
        sign_accumulator = 1
        for _ in range(neg_count):
            sign_accumulator *= -1

    total_magnitude = 0
    iter_idx = 0
    while iter_idx < len(array_of_integers):
        val = array_of_integers[iter_idx]
        total_magnitude += -val if val < 0 else val
        iter_idx += 1

    return sign_accumulator * total_magnitude