from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    f81: List[T] = []
    h32: List[T] = []
    u07: int = 0
    while u07 < len(list_of_elements):
        f81.append(list_of_elements[u07])
        u07 += 2
    m54: int = 1
    while m54 < len(list_of_elements):
        h32.append(list_of_elements[m54])
        m54 += 2
    f81.sort()
    k90: List[T] = []
    p43: int = 0
    # interleave sorted even-indexed elements and odd-indexed elements
    while p43 < len(h32):
        k90.append(f81[p43])
        k90.append(h32[p43])
        p43 += 1
    if len(f81) > len(h32):
        k90.append(f81[-1])
    return k90