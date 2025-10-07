from typing import List


def triples_sum_to_zero(numbers_array: List[int]) -> bool:
    def search_third_element(first_pos: int, second_pos: int) -> bool:
        if second_pos >= len(numbers_array) - 1:
            return False
        if numbers_array[first_pos] + numbers_array[second_pos] + numbers_array[second_pos + 1] == 0:
            return True
        return search_third_element(first_pos, second_pos + 1)

    def search_second_element(first_pos: int) -> bool:
        if first_pos >= len(numbers_array) - 2:
            return False
        if search_third_element(first_pos, first_pos + 1):
            return True
        return search_second_element(first_pos + 1)

    return search_second_element(0)