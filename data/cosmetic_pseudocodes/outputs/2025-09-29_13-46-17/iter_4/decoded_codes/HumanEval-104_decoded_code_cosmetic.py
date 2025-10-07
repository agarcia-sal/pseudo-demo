from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    OddDigitAccumulator: List[int] = []

    def check_all_odd(index: int) -> None:
        if index >= len(list_of_positive_integers):
            return
        current_value = list_of_positive_integers[index]
        digit_list: List[int] = []
        temp_val = current_value
        while temp_val > 0:
            digit_list.insert(0, temp_val % 10)  # prepend digit
            temp_val //= 10
        has_even_digit = False
        for digit in digit_list:
            if digit % 2 == 0:
                has_even_digit = True
                break
        if not has_even_digit:
            OddDigitAccumulator.append(current_value)
        check_all_odd(index + 1)

    check_all_odd(0)

    def compare_asc(lhs: int, rhs: int) -> bool:
        return lhs < rhs

    sorted_result: List[int] = []
    while len(OddDigitAccumulator) > 0:
        min_val = OddDigitAccumulator[0]
        min_idx = 0
        for i in range(1, len(OddDigitAccumulator)):
            if not compare_asc(min_val, OddDigitAccumulator[i]):
                min_val = OddDigitAccumulator[i]
                min_idx = i
        OddDigitAccumulator.pop(min_idx)
        sorted_result.append(min_val)

    return sorted_result