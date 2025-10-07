from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    a1: List[T] = []
    b2: List[T] = []
    i: int = 0
    while i < len(list_of_elements):
        if i % 2 == 0:
            a1.append(list_of_elements[i])
        else:
            b2.append(list_of_elements[i])
        i += 1

    x9: int = len(a1)
    y8: int = len(b2)

    j7: int = 1
    while j7 < x9:
        k6: int = j7
        while k6 > 0 and a1[k6 - 1] > a1[k6]:
            a1[k6], a1[k6 - 1] = a1[k6 - 1], a1[k6]
            k6 -= 1
        j7 += 1

    result4: List[T] = []
    m3: int = 0
    while m3 < y8:
        result4.append(a1[m3])
        result4.append(b2[m3])
        m3 += 1

    if x9 > y8:
        result4.append(a1[x9 - 1])

    return result4