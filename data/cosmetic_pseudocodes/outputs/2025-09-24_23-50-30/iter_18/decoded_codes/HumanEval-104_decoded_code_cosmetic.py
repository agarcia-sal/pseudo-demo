from typing import List

def unique_digits(collection_of_positive_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index < len(collection_of_positive_numbers):
        candidate: int = collection_of_positive_numbers[index]
        digit_index: int = 0
        has_even_digit: bool = False
        candidate_str: str = str(candidate)
        while digit_index < len(candidate_str):
            digit_char: str = candidate_str[digit_index]
            digit_value: int = int(digit_char)
            if (digit_value // 2) * 2 == digit_value:
                has_even_digit = True
                break
            digit_index += 1
        if not has_even_digit:
            accumulator.append(candidate)
        index += 1

    sorted_result: List[int] = []
    while len(accumulator) > 0:
        min_value: int = accumulator[0]
        pos: int = 0
        scan: int = 1
        while scan < len(accumulator):
            if accumulator[scan] < min_value:
                min_value = accumulator[scan]
                pos = scan
            scan += 1
        sorted_result.append(min_value)
        accumulator = accumulator[:pos] + accumulator[pos+1:]
    return sorted_result