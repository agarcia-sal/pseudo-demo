from typing import List


def add(list_of_integers: List[int]) -> int:
    list_of_selected_elements: List[int] = [
        list_of_integers[index]
        for index in range(1, len(list_of_integers), 2)
        if list_of_integers[index] % 2 == 0
    ]
    sum_of_selected_elements: int = sum(list_of_selected_elements)
    return sum_of_selected_elements