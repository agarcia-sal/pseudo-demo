from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    elements_collector: List[int] = []
    for number in list_of_integers:
        if number not in elements_collector:
            elements_collector.append(number)
    sorted_elements = elements_collector[:]
    while True:
        swapped = False
        for index in range(len(sorted_elements) - 1):
            if sorted_elements[index] > sorted_elements[index + 1]:
                sorted_elements[index], sorted_elements[index + 1] = sorted_elements[index + 1], sorted_elements[index]
                swapped = True
        if not swapped:
            break

    if len(sorted_elements) <= 1:
        return None
    return sorted_elements[1]