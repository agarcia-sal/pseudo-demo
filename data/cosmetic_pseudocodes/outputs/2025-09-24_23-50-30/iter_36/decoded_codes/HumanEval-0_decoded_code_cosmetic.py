from typing import List, NamedTuple


class IndexedPair(NamedTuple):
    index: int
    value: float


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pairs(idx_a: int, val_a: float, idx_b: int, val_b: float) -> bool:
        return (idx_a != idx_b) and (abs(val_a - val_b) < threshold_value)

    def iterate_j(idx_i: int, val_i: float, arr_j: List[IndexedPair]) -> bool:
        if not arr_j:
            return False
        current_j, rest_j = arr_j[0], arr_j[1:]
        if check_pairs(idx_i, val_i, current_j.index, current_j.value):
            return True
        return iterate_j(idx_i, val_i, rest_j)

    def iterate_i(arr_i: List[IndexedPair], arr_j: List[IndexedPair]) -> bool:
        if not arr_i:
            return False
        pair, rest_i = arr_i[0], arr_i[1:]
        if iterate_j(pair.index, pair.value, arr_j):
            return True
        return iterate_i(rest_i, arr_j)

    indexed_pairs = [IndexedPair(i, val) for i, val in enumerate(list_of_numbers)]
    return iterate_i(indexed_pairs, indexed_pairs)