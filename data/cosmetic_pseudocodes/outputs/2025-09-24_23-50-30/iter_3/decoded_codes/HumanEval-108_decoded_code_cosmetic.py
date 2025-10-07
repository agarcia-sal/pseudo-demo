from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign = -1

        digits_str = str(integer_value)
        digits_arr = [int(ch) for ch in digits_str]

        digits_arr[0] *= sign

        total = 0
        idx = 0
        while idx < len(digits_arr):
            total += digits_arr[idx]
            idx += 1

        return total

    results: List[int] = []
    idx = 0
    for _ in range(len(array_of_integers)):
        results.append(digits_sum(array_of_integers[idx]))
        idx += 1

    positive_values = [val for val in results if val > 0]

    return len(positive_values)