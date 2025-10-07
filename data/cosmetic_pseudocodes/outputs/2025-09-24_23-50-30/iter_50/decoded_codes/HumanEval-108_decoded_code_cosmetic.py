from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_flag: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign_flag = -1

        digit_str: str = str(integer_value)
        converted_digits: List[int] = [int(d) for d in digit_str]

        converted_digits[0] = converted_digits[0] * sign_flag

        accumulator: int = sum(converted_digits)
        return accumulator

    def helper(accum_results: List[int], remaining_numbers: List[int]) -> List[int]:
        if not remaining_numbers:
            return accum_results
        head: int = remaining_numbers[0]
        tail: List[int] = remaining_numbers[1:]
        return helper(accum_results + [digits_sum(head)], tail)

    sums_list: List[int] = helper([], array_of_integers)

    def select_positive(collection: List[int]) -> List[int]:
        positive_elements: List[int] = [element for element in collection if element > 0]
        return positive_elements

    return len(select_positive(sums_list))