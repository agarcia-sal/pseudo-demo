from typing import List


def order_by_points(collection_of_values: List[int]) -> List[int]:
    def digits_sum(value: int) -> int:
        polarity = 1
        while value < 0:
            value = -value
            polarity = -polarity
            break  # only invert once, then exit loop

        digits_array: List[int] = []
        temp_value = value

        if temp_value == 0:
            digits_array.append(0)
        else:
            while temp_value > 0:
                digits_array.append(temp_value % 10)
                temp_value //= 10

        digits_array[0] *= polarity  # apply polarity to the first digit

        total_sum = 0
        cursor = 0
        while cursor < len(digits_array):
            total_sum += digits_array[cursor]
            cursor += 1

        return total_sum

    def comparator(a: int, b: int) -> bool:
        return digits_sum(a) < digits_sum(b)

    index_i = 1
    while index_i < len(collection_of_values):
        index_j = index_i
        while index_j > 0 and comparator(collection_of_values[index_j], collection_of_values[index_j - 1]):
            collection_of_values[index_j], collection_of_values[index_j - 1] = (
                collection_of_values[index_j - 1],
                collection_of_values[index_j],
            )
            index_j -= 1
        index_i += 1

    return collection_of_values