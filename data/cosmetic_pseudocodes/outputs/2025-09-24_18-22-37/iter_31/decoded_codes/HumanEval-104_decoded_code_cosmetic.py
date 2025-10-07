from typing import List


def unique_digits(sequence_of_numbers: List[int]) -> List[int]:
    candidates: List[int] = []
    idx: int = 0
    while idx < len(sequence_of_numbers):
        current_number: int = sequence_of_numbers[idx]
        all_digits_odd: bool = True
        str_repr: str = str(current_number)
        char_pos: int = 0
        while char_pos < len(str_repr) and all_digits_odd:
            digit_char: str = str_repr[char_pos]
            digit_value: int = ord(digit_char) - ord('0')
            if (digit_value % 2) == 0:
                all_digits_odd = False
            char_pos += 1
        if all_digits_odd:
            candidates.append(current_number)
        idx += 1
    sorted_result: List[int] = sorted(candidates)
    return sorted_result