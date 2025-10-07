from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign = -1

        digits_str = str(integer_value)
        digits_list: List[int] = []

        def convert_chars_to_ints(idx: int, digit_chars: str) -> None:
            if idx == len(digit_chars):
                return
            digits_list.append(int(digit_chars[idx]))
            convert_chars_to_ints(idx + 1, digit_chars)

        convert_chars_to_ints(0, digits_str)

        digits_list[0] *= sign

        def sum_recursive(items: List[int], pos: int) -> int:
            if pos >= len(items):
                return 0
            return items[pos] + sum_recursive(items, pos + 1)

        return sum_recursive(digits_list, 0)

    def build_digit_sums_list(numbers: List[int], idx: int, result: List[int]) -> List[int]:
        if idx >= len(numbers):
            return result
        result.append(digits_sum(numbers[idx]))
        return build_digit_sums_list(numbers, idx + 1, result)

    all_sums = build_digit_sums_list(array_of_integers, 0, [])

    def count_positives(arr: List[int], index: int, count: int) -> int:
        if index >= len(arr):
            return count
        if arr[index] > 0:
            return count_positives(arr, index + 1, count + 1)
        return count_positives(arr, index + 1, count)

    return count_positives(all_sums, 0, 0)