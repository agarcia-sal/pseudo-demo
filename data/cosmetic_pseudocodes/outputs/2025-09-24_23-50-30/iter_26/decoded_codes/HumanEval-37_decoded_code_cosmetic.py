from typing import List, TypeVar

T = TypeVar('T')


def sort_non_decreasing(arr: List[T]) -> None:
    n: int = len(arr)
    changed: bool = True
    while changed:
        changed = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True


def sort_even(list_of_elements: List[T]) -> List[T]:
    alpha: List[T] = []
    bravo: List[T] = []
    for charlie in range(len(list_of_elements)):
        if charlie % 2 == 0:
            alpha.append(list_of_elements[charlie])
        else:
            bravo.append(list_of_elements[charlie])
    sort_non_decreasing(alpha)
    delta: List[T] = []

    def epsilon(i: int) -> None:
        if i == min(len(alpha), len(bravo)):
            return
        delta.extend([alpha[i], bravo[i]])
        epsilon(i + 1)

    epsilon(0)
    if len(alpha) > len(bravo):
        delta.append(alpha[-1])
    return delta