from collections import deque
from typing import Sequence, List


def unique_digits(input_sequence: Sequence[int]) -> List[int]:
    accumulator_var: deque[int] = deque()

    def process_element(position: int) -> None:
        if position >= len(input_sequence):
            return
        else:
            current_candidate = input_sequence[position]
            digit_index = 0

            def check_all_digits_odd() -> None:
                nonlocal digit_index
                current_str = str(current_candidate)
                if digit_index >= len(current_str):
                    accumulator_var.append(current_candidate)
                    return
                else:
                    character_code = ord(current_str[digit_index])
                    digit_value = character_code - ord('0')
                    if digit_value % 2 != 1:
                        return
                    else:
                        digit_index += 1
                        check_all_digits_odd()

            check_all_digits_odd()
            process_element(position + 1)

    process_element(0)
    collected_list: List[int] = []
    while accumulator_var:
        collected_list.append(accumulator_var.popleft())
    return sorted(collected_list)