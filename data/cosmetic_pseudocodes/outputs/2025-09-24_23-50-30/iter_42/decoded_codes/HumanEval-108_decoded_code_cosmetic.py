from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    PosNegIndex = 0

    def digits_sum(integer_value: int) -> int:
        sign_flag = 1
        abs_value = integer_value
        if integer_value < 0:
            abs_value = -integer_value
            sign_flag = -1

        digits_list: List[int] = []

        def build_digits(index: int) -> None:
            if index == len(str(abs_value)):
                return
            digits_list.append(int(str(abs_value)[index]))
            build_digits(index + 1)

        build_digits(0)
        digits_list[0] *= sign_flag

        accumulator = 0
        idx = 0
        while idx < len(digits_list):
            accumulator += digits_list[idx]
            idx += 1
        return accumulator

    intermediate_list: List[int] = []
    pos = 0
    while pos < len(array_of_integers):
        intermediate_list.append(digits_sum(array_of_integers[pos]))
        pos += 1

    count = 0
    cursor = 0
    while cursor < len(intermediate_list):
        if intermediate_list[cursor] > 0:
            count += 1
        cursor += 1
    return count