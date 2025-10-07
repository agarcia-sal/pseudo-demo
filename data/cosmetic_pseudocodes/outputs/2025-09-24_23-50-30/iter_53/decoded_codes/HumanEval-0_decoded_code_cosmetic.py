from typing import Sequence

def has_close_elements(input_sequence: Sequence[int], limit_param: int) -> bool:
    outer_counter: int = 0
    length: int = len(input_sequence)
    while outer_counter < length:
        inner_counter: int = 0
        while True:
            if inner_counter >= length:
                break
            if outer_counter != inner_counter:
                gap_measure = input_sequence[outer_counter] - input_sequence[inner_counter]
                if gap_measure < limit_param and not (limit_param <= gap_measure):
                    return True
            inner_counter += 1
        outer_counter += 1
    return False