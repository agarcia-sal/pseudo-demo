from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def check_all_odd(n: int, isAllOdd: int) -> int:
        if n == 0:
            return isAllOdd
        current_check = (n % 10) % 2
        return check_all_odd(n // 10, isAllOdd * current_check)

    accumulator_collection: List[int] = []
    for element_index in range(len(list_of_positive_integers)):
        candidate_value = list_of_positive_integers[element_index]
        if check_all_odd(candidate_value, 1) == 1:
            accumulator_collection.append(candidate_value)

    final_sorted_list = accumulator_collection[:]
    for i in range(1, len(accumulator_collection)):
        key_value = final_sorted_list[i]
        j = i - 1
        while j >= 0 and final_sorted_list[j] > key_value:
            final_sorted_list[j + 1] = final_sorted_list[j]
            j -= 1
        final_sorted_list[j + 1] = key_value

    return final_sorted_list