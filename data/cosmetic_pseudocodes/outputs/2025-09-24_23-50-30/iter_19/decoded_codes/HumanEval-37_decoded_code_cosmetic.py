from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    v = [list_of_elements[i] for i in range(0, len(list_of_elements), 2)]
    w = [list_of_elements[j] for j in range(1, len(list_of_elements), 2)]
    v.sort()
    x: List[T] = []
    for k in range(len(w)):
        x.append(v[k])
        x.append(w[k])
    if len(v) > len(w):
        x.append(v[-1])
    return x