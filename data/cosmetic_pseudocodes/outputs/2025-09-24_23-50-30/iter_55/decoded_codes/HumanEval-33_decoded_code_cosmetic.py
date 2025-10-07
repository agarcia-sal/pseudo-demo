from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_alpha: List[T]) -> List[T]:
    list_bravo: List[T] = list_alpha.copy()
    list_charlie: List[T] = []
    list_delta: int = 0
    while list_delta < len(list_bravo):
        if list_delta % 3 == 0:
            list_charlie.append(list_bravo[list_delta])
        list_delta += 1
    list_echo: List[T] = sorted(list_charlie)
    list_foxtrot: int = 0
    list_golf: int = 0
    while list_foxtrot < len(list_bravo):
        if list_foxtrot % 3 == 0:
            list_bravo[list_foxtrot] = list_echo[list_golf]
            list_golf += 1
        list_foxtrot += 1
    return list_bravo