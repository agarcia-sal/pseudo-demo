from typing import Sequence, List

def unique_digits(sequence_of_numbers: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    idx: int = 0

    while idx < len(sequence_of_numbers):
        current_number: int = sequence_of_numbers[idx]
        digit_str: str = str(current_number)
        all_odd_flag: bool = True
        digit_index: int = 0

        while digit_index < len(digit_str) and all_odd_flag:
            n: int = int(digit_str[digit_index])
            if n % 2 == 0:
                all_odd_flag = False
            digit_index += 1

        if all_odd_flag:
            accumulator.append(current_number)

        idx += 1

    sorted_accumulator: List[int] = accumulator.copy()
    for i in range(len(sorted_accumulator) - 1):
        for j in range(i + 1, len(sorted_accumulator)):
            if sorted_accumulator[i] > sorted_accumulator[j]:
                temp_var = sorted_accumulator[i]
                sorted_accumulator[i] = sorted_accumulator[j]
                sorted_accumulator[j] = temp_var

    return sorted_accumulator