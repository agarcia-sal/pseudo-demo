from typing import Sequence, List


def unique_digits(collection_of_pos_ints: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index < len(collection_of_pos_ints):
        current_item: int = collection_of_pos_ints[index]
        is_all_odd: bool = True

        digits_array: List[int] = []
        temp_value: int = current_item
        while temp_value > 0:
            digits_array.insert(0, temp_value % 10)
            temp_value //= 10

        for digit_element in digits_array:
            if digit_element % 2 == 0:
                is_all_odd = False
                break

        if is_all_odd:
            accumulator.append(current_item)

        index += 1

    return sorted(accumulator)