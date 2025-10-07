from typing import List


def tri(integer_n: int) -> List[float]:
    if integer_n == 0:
        return [1]

    result_sequence: List[float] = [1, 3]

    def recursive_append(current_index: int) -> None:
        if current_index > integer_n:
            return

        if current_index % 2 == 0:
            half_incremented = (current_index / 2) + 1
            result_sequence.append(half_incremented)
        else:
            val1 = result_sequence[current_index - 1]
            val2 = result_sequence[current_index - 2]
            half_plus_three = (current_index + 3) / 2
            combined_value = val1 + val2 + half_plus_three
            result_sequence.append(combined_value)

        recursive_append(current_index + 1)

    recursive_append(2)

    return result_sequence