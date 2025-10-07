from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        factor = 1
        if integer_value < 0:
            integer_value = -integer_value
            factor = -1

        digits_array: List[int] = [int(ch) for ch in str(integer_value)]
        digits_array[0] *= factor

        total = 0
        for digit in digits_array:
            total += digit

        return total

    sums_collection: List[int] = []
    for current_num in array_of_integers:
        sum_val = digits_sum(current_num)
        sums_collection.append(sum_val)

    positive_sums: List[int] = [val for val in sums_collection if val > 0]

    return len(positive_sums)