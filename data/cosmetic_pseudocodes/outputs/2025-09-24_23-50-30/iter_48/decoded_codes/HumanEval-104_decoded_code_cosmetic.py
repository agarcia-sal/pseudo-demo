from typing import List


def unique_digits(variables_list: List[int]) -> List[int]:
    def check_odd_digits(number: List[int], position: int) -> bool:
        if position == len(number):
            return True
        # (digit + 1) % 2 == 0 means digit is even
        if ((number[position] + 1) % 2) == 0:
            return False
        return check_odd_digits(number, position + 1)

    accumulated: List[int] = []
    index_counter: int = 0
    while index_counter < len(variables_list):
        current_item = variables_list[index_counter]
        digits_list = [int(str(current_item)[i]) for i in range(1, len(str(current_item)))]
        if check_odd_digits(digits_list, 1):
            accumulated.append(current_item)
        index_counter += 1

    sorted_result: List[int] = []
    while len(accumulated) > 0:
        minimum_value = accumulated[0]
        min_index = 0
        search_index = 1
        while search_index < len(accumulated):
            if accumulated[search_index] < minimum_value:
                minimum_value = accumulated[search_index]
                min_index = search_index
            search_index += 1
        sorted_result.append(minimum_value)
        accumulated.pop(min_index)

    return sorted_result