from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    result_list: List[int] = []
    sorted_values: List[int] = array_of_integers[:]

    if positive_integer_k == 0:
        return result_list

    sort_ascending(sorted_values)

    index_limit: int = len(sorted_values) - positive_integer_k
    if index_limit < 0:
        # If k is larger than list length, return entire list (all max)
        index_limit = 0

    for integer_variable in range(index_limit, len(sorted_values)):
        result_list.append(sorted_values[integer_variable])

    return result_list


def sort_ascending(list_of_values: List[int]) -> None:
    n = len(list_of_values)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if not (list_of_values[j] <= list_of_values[j + 1]):
                temp_var = list_of_values[j]
                list_of_values[j] = list_of_values[j + 1]
                list_of_values[j + 1] = temp_var