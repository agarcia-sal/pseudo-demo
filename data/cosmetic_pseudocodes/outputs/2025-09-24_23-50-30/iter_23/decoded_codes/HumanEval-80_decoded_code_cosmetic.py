from typing import Sequence

def is_happy(data_sequence: Sequence[object]) -> bool:
    data_length = len(data_sequence)
    if data_length < 3:
        return False

    def check_group(position: int) -> bool:
        if position > data_length - 3:
            return True
        first = data_sequence[position]
        second = data_sequence[position + 1]
        third = data_sequence[position + 2]
        if first == second or second == third or first == third:
            return False
        return check_group(position + 1)

    return check_group(0)