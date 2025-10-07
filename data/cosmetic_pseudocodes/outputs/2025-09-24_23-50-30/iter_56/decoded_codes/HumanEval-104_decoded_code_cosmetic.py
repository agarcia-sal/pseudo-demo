from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:

    def digits_all_odd(number_param: int) -> bool:

        def aux_check_odd(dividend_param: int) -> bool:
            if dividend_param == 0:
                return True
            if (dividend_param % 10) % 2 == 0:
                return False
            return aux_check_odd(dividend_param // 10)

        return aux_check_odd(number_param)

    accumulation_list: List[int] = []
    iteration_index: int = 0
    upper_limit: int = len(list_of_positive_integers)

    while iteration_index != upper_limit:
        current_candidate = list_of_positive_integers[iteration_index]
        if digits_all_odd(current_candidate):
            accumulation_list.append(current_candidate)
        iteration_index += 1

    return sorted(accumulation_list)