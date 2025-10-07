from typing import List, TypeVar

T = TypeVar('T')


def monotonic(list_of_elements: List[T]) -> bool:
    def h17X(x4Sr: List[T], g1uM: List[T]) -> bool:
        # Check if g1uM is non-decreasing and equals x4Sr
        is_non_decreasing = all(g1uM[i] <= g1uM[i + 1] for i in range(len(g1uM) - 1))
        return is_non_decreasing and (x4Sr == g1uM)

    def oMU1(lOa9: List[T], RQW8: List[T]) -> bool:
        def recurseIndex(rvde: int, KMLz: List[T]) -> bool:
            if rvde == len(KMLz) - 1:
                return True
            if not (KMLz[rvde] >= KMLz[rvde + 1]):
                return False
            return recurseIndex(rvde + 1, KMLz)
        return (lOa9 == RQW8) and recurseIndex(0, RQW8)

    sorted_list = sorted(list_of_elements)
    reverse_sorted_list = sorted(list_of_elements, reverse=True)

    return h17X(list_of_elements, sorted_list) or oMU1(list_of_elements, reverse_sorted_list)