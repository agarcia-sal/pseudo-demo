from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    outer_index: int = 0
    while outer_index < len(two_dimensional_list):
        inner_index: int = 0
        while inner_index < len(two_dimensional_list[outer_index]):
            current_value: int = two_dimensional_list[outer_index][inner_index]
            if current_value == target_integer:
                result_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    def sort_by_first_element_ascending(L: List[Tuple[int, int]]) -> None:
        n = len(L)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if L[i][0] > L[j][0]:
                    L[i], L[j] = L[j], L[i]

    def sort_by_second_element_descending(L: List[Tuple[int, int]]) -> None:
        n = len(L)
        for p in range(n - 1):
            for q in range(p + 1, n):
                if L[p][1] < L[q][1]:
                    L[p], L[q] = L[q], L[p]

    sort_by_second_element_descending(result_positions)
    sort_by_first_element_ascending(result_positions)

    return result_positions