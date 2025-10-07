from typing import List

def count_nums(number_sequence: List[int]) -> int:
    def digits_sum(value: int) -> int:
        flag = 1
        if value < 0:
            value = -value
            flag = -1
        str_digits = str(value)
        # Convert string digits to int digits; index 0-based in Python
        digits_array = [int(ch) for ch in str_digits]
        if digits_array:
            digits_array[0] *= flag  # apply sign to first digit
        total = sum(digits_array)
        return total

    def map_digits_sum(names: List[int], acc: List[int]) -> List[int]:
        if not names:
            return acc[::-1]  # reverse acc
        head, tail = names[0], names[1:]
        return map_digits_sum(tail, acc + [digits_sum(head)])

    sums_list = map_digits_sum(number_sequence, [])
    positives = [item for item in sums_list if item > 0]
    return len(positives)