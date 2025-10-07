from typing import List, Dict


def count_nums(array_of_integers: List[int]) -> int:

    def digits_sum(integer_value: int) -> int:
        abs_value: int = integer_value
        sign_flag: int = 1
        if integer_value < 0:
            abs_value = -integer_value
            sign_flag = -1

        digit_chars: List[str] = list(str(abs_value))
        transformed_digits: List[int] = [0] * len(digit_chars)
        index_dummy: int = 0
        while index_dummy < len(digit_chars):
            transformed_digits[index_dummy] = int(digit_chars[index_dummy])
            index_dummy += 1

        transformed_digits[0] *= sign_flag

        total_sum: int = 0
        idx_cursor: int = 0
        while idx_cursor < len(transformed_digits):
            total_sum += transformed_digits[idx_cursor]
            idx_cursor += 1

        return total_sum

    digit_sums_dict: Dict[int, int] = {}
    idx_counter: int = 0
    while idx_counter < len(array_of_integers):
        current_elem = array_of_integers[idx_counter]
        digit_sums_dict[idx_counter] = digits_sum(current_elem)
        idx_counter += 1

    positive_sum_count: int = 0
    keys_list = list(digit_sums_dict.keys())
    key_iterator: int = 0
    while key_iterator < len(keys_list):
        k = keys_list[key_iterator]
        if digit_sums_dict[k] > 0:
            positive_sum_count += 1
        key_iterator += 1

    return positive_sum_count