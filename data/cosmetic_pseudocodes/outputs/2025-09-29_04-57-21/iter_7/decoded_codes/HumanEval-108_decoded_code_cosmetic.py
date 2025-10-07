from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        polarity = 1
        if integer_value < 0:
            integer_value = -integer_value
            polarity = -1
        digits_list = [int(ch) for ch in str(integer_value)]
        digits_list[0] *= polarity

        total = 0
        iterator = 0
        while iterator < len(digits_list):
            total += digits_list[iterator]
            iterator += 1
        return total

    sums_collection: List[int] = []
    pos = 0
    while pos < len(array_of_integers):
        sums_collection.append(digits_sum(array_of_integers[pos]))
        pos += 1

    positive_values: List[int] = []
    for val in sums_collection:
        if val > 0:
            positive_values.append(val)

    return len(positive_values)