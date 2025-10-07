from typing import List, Tuple

def digits(n: int) -> int:
    def process_chars(index: int, accum_product: int, count_odds: int, char_array: List[str]) -> Tuple[int, int]:
        if index >= len(char_array):
            return accum_product, count_odds
        current_char = char_array[index]
        digit_val = int(current_char)
        if digit_val % 2 == 1:
            return process_chars(index + 1, accum_product * digit_val, count_odds + 1, char_array)
        else:
            return process_chars(index + 1, accum_product, count_odds, char_array)

    chars_list = list(str(n))
    final_product, final_odd_count = process_chars(0, 1, 0, chars_list)
    return 0 if final_odd_count == 0 else final_product