from typing import Sequence

def digitSum(input_sequence: Sequence[str]) -> int:
    if input_sequence == "":
        return 0
    total_value = 0
    for element in input_sequence:
        if 'A' <= element <= 'Z':
            total_value += ord(element)
    return total_value