from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        temporary_multiplier: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            temporary_multiplier = -1

        digits_list: str = str(integer_value)
        digits_collection: List[int] = [int(d) for d in digits_list]

        # Apply temporary_multiplier to first digit
        digits_collection[0] *= temporary_multiplier

        sum_total: int = sum(digits_collection)
        return sum_total

    secondary_list: List[int] = [digits_sum(num) for num in array_of_integers]
    filtered_collection: List[int] = [val for val in secondary_list if val > 0]

    return len(filtered_collection)