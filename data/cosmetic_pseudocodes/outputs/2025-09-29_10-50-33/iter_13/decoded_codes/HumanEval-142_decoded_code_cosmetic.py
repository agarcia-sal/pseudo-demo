from typing import Sequence


def sum_squares(collection_of_numbers: Sequence[int]) -> int:
    result_values: list[int] = []
    current_position: int = 0
    length = len(collection_of_numbers)

    while current_position < length:
        if current_position % 3 == 0:
            # square when position divisible by 3
            result_values.append(collection_of_numbers[current_position] ** 2)
        else:
            if (current_position % 4 == 0) and (current_position % 3 != 0):
                # cube when divisible by 4 and not by 3
                result_values.append(collection_of_numbers[current_position] ** 3)
            else:
                # otherwise just append as-is
                result_values.append(collection_of_numbers[current_position])
        current_position += 1

    total_sum: int = 0
    position_in_result: int = 0
    length_result = len(result_values)

    while position_in_result < length_result:
        total_sum += result_values[position_in_result]
        position_in_result += 1

    return total_sum