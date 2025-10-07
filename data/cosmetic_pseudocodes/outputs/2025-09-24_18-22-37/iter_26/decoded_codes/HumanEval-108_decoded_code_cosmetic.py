from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_factor = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign_factor = -1
        integer_str = str(integer_value)
        digit_chars = list(integer_str)
        temp_list: List[int] = []
        idx = 0
        while idx < len(digit_chars):
            char = digit_chars[idx]
            num_val = int(char)
            if idx == 0:
                num_val *= sign_factor
            temp_list.append(num_val)
            idx += 1
        total_sum = 0
        for value in temp_list:
            total_sum += value
        return total_sum

    sums_collection: List[int] = []
    pos = 0
    while pos < len(array_of_integers):
        current_item = array_of_integers[pos]
        sums_collection.append(digits_sum(current_item))
        pos += 1

    positive_items: List[int] = []
    for val in sums_collection:
        if val > 0:
            positive_items.append(val)
    return len(positive_items)