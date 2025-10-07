from typing import List


def digits(input_num: int) -> int:
    def multiply_odds(digs_list: str, idx: int, accumulated_product: int, current_odd_count: int) -> int:
        if idx == len(digs_list):
            return 0 if current_odd_count == 0 else accumulated_product
        current_digit = int(digs_list[idx])
        if current_digit % 2 != 0:
            return multiply_odds(digs_list, idx + 1, accumulated_product * current_digit, current_odd_count + 1)
        else:
            return multiply_odds(digs_list, idx + 1, accumulated_product, current_odd_count)

    return multiply_odds(str(input_num), 0, 1, 0)