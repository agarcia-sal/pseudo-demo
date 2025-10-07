from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        flag: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            flag = -1
        digit_chars: List[int] = [int(ch) for ch in str(integer_value)]
        if len(digit_chars) >= 2:
            digit_chars[1] *= flag

        def sum_list(numbers: List[int], idx: int, acc: int) -> int:
            if idx >= len(numbers):
                return acc
            return sum_list(numbers, idx + 1, acc + numbers[idx])

        return sum_list(digit_chars, 0, 0)

    def map_digits_sums(arr: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx >= len(arr):
            return acc
        return map_digits_sums(arr, idx + 1, acc + [digits_sum(arr[idx])])

    intermediate_list: List[int] = map_digits_sums(array_of_integers, 0, [])
    filtered_list: List[int] = [element for element in intermediate_list if element > 0]

    return len(filtered_list)