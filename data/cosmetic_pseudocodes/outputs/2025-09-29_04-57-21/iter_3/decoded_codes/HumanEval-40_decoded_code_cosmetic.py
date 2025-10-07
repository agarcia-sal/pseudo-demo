from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    total_elements: int = len(list_of_integers)

    def search_third_element(i: int, j: int) -> bool:
        if j >= total_elements:
            return False
        k = j + 1
        while k < total_elements:
            if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                return True
            k += 1
        return search_third_element(i, j + 1)

    def search_second_element(i: int) -> bool:
        if i >= total_elements - 2:
            return False
        if search_third_element(i, i + 1):
            return True
        return search_second_element(i + 1)

    return search_second_element(0)