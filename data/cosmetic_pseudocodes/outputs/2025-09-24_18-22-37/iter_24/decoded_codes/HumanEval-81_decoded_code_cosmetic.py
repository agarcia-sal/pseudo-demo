from typing import List


def numerical_letter_grade(arr_numbers: List[float]) -> List[str]:
    arr_letters: List[str] = []
    idx_counter: int = 0
    length: int = len(arr_numbers)
    while idx_counter < length:
        val_curr: float = arr_numbers[idx_counter]
        is_continue: bool = True
        if val_curr == 4.0:
            arr_letters.append("A+")
            is_continue = False
        if val_curr > 3.7 and is_continue:
            arr_letters.append("A")
            is_continue = False
        if val_curr > 3.3 and is_continue:
            arr_letters.append("A-")
            is_continue = False
        if val_curr > 3.0 and is_continue:
            arr_letters.append("B+")
            is_continue = False
        if val_curr > 2.7 and is_continue:
            arr_letters.append("B")
            is_continue = False
        if val_curr > 2.3 and is_continue:
            arr_letters.append("B-")
            is_continue = False
        if val_curr > 2.0 and is_continue:
            arr_letters.append("C+")
            is_continue = False
        if val_curr > 1.7 and is_continue:
            arr_letters.append("C")
            is_continue = False
        if val_curr > 1.3 and is_continue:
            arr_letters.append("C-")
            is_continue = False
        if val_curr > 1.0 and is_continue:
            arr_letters.append("D+")
            is_continue = False
        if val_curr > 0.7 and is_continue:
            arr_letters.append("D")
            is_continue = False
        if val_curr > 0.0 and is_continue:
            arr_letters.append("D-")
            is_continue = False
        if is_continue:
            arr_letters.append("E")
        idx_counter += 1
    return arr_letters