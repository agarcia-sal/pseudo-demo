from typing import Iterable, List

def unique_digits(sequence_of_numbers: Iterable[int]) -> List[int]:
    accumulator: List[int] = []
    for value in sequence_of_numbers:
        flag: bool = True
        digits_array: List[str] = list(str(value))
        index: int = 0
        while index < len(digits_array) and flag:
            if int(digits_array[index]) % 2 == 0:
                flag = False
            index += 1
        if flag:
            accumulator.append(value)
    return sorted(accumulator)