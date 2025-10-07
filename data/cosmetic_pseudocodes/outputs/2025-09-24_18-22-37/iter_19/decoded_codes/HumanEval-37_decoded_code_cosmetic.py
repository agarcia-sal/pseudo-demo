from typing import List, Union

def sort_even(list_of_elements: List[Union[int, float]]) -> List[Union[int, float]]:
    accumulator: List[Union[int, float]] = []
    x: List[Union[int, float]] = []
    y: List[Union[int, float]] = []

    i = 0
    while i < len(list_of_elements):
        x.append(list_of_elements[i])
        i += 2

    j = 1
    while j < len(list_of_elements):
        y.append(list_of_elements[j])
        j += 2

    x.sort()  # sort non-decreasing

    k = 0
    while True:
        if k < len(y):
            z = (x[k], y[k])
            accumulator.extend(z)
        else:
            break
        k += 1

    if len(x) > len(y):
        accumulator.append(x[-1])

    return accumulator