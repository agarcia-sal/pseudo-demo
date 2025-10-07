from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        digits_chars: str = str(integer_value)
        digits_list: List[int] = [int(d) for d in digits_chars]

        digits_list[0] = digits_list[0] * multiplier_sign

        return sum(digits_list)

    collection_sums: List[int] = []
    index_tracker: int = 0
    while index_tracker < len(array_of_integers):
        current_integer = array_of_integers[index_tracker]
        sum_for_current = digits_sum(current_integer)
        collection_sums.append(sum_for_current)
        index_tracker += 1

    filtered_collection = [candidate for candidate in collection_sums if candidate > 0]

    return len(filtered_collection)