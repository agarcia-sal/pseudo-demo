from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    alpha = [list_of_elements[i] for i in range(0, len(list_of_elements), 2)]
    beta = [list_of_elements[i] for i in range(1, len(list_of_elements), 2)]

    # gamma_sort sorts the list in place
    def gamma_sort(lst: List[T]) -> None:
        lst.sort()

    gamma_sort(alpha)

    def zeta(pairs: List[tuple[T, T]], acc: List[T]) -> List[T]:
        if not pairs:
            return acc
        head_pair, *tail_pairs = pairs
        new_acc = acc + [head_pair[0], head_pair[1]]
        return zeta(tail_pairs, new_acc)

    delta: List[T] = []
    delta = zeta(list(zip(alpha, beta)), delta)

    if len(alpha) > len(beta):
        delta.append(alpha[-1])

    return delta