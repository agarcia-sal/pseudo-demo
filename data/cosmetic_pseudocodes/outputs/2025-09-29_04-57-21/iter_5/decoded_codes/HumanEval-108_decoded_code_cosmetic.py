from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_flag = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign_flag = -1

        digit_seq = list(str(integer_value))
        # Multiply the first digit by sign_flag to preserve sign as int
        digit_seq[0] = str(int(digit_seq[0]) * sign_flag)
        total = 0
        for digit in digit_seq:
            total += int(digit)
        return total

    sums_collection: List[int] = []
    idx_counter = 0
    while idx_counter < len(array_of_integers):
        sums_collection.append(digits_sum(array_of_integers[idx_counter]))
        idx_counter += 1

    positive_items: List[int] = []
    for item in sums_collection:
        if item > 0:
            positive_items.append(item)

    return len(positive_items)