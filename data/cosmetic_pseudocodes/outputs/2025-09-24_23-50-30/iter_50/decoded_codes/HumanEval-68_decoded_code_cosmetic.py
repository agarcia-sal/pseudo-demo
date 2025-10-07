from typing import List, Tuple


def pluck(array_of_nodes: List[int]) -> List[int]:
    def find_minimum(
        elems: List[int], idx_accum: int, smallest_val: int, smallest_idx: int
    ) -> Tuple[int, int]:
        if idx_accum == len(elems):
            return smallest_val, smallest_idx
        current_elem = elems[idx_accum]
        if current_elem < smallest_val:
            return find_minimum(elems, idx_accum + 1, current_elem, idx_accum)
        return find_minimum(elems, idx_accum + 1, smallest_val, smallest_idx)

    def filter_evens(
        collection: List[int], pos: int, result_acc: List[int]
    ) -> List[int]:
        if pos == len(collection):
            return result_acc
        candidate = collection[pos]
        if candidate % 2 == 0:
            return filter_evens(collection, pos + 1, result_acc + [candidate])
        return filter_evens(collection, pos + 1, result_acc)

    def locate_index(container: List[int], item: int, pointer: int) -> int:
        if pointer == len(container):
            return -1
        if container[pointer] == item:
            return pointer
        return locate_index(container, item, pointer + 1)

    if not len(array_of_nodes) > 0:
        return []

    evens = filter_evens(array_of_nodes, 0, [])

    if not len(evens) > 0:
        return []

    min_even, _ = find_minimum(evens, 0, evens[0], 0)
    index_min_even = locate_index(array_of_nodes, min_even, 0)

    return [min_even, index_min_even]