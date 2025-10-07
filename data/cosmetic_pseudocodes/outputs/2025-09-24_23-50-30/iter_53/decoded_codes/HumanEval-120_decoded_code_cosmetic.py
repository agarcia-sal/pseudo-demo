from typing import List, TypeVar, Sequence

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: object) -> bool:
        return NotImplemented

def maximum(data_container: List[T], count_limit: int) -> List[T]:
    if count_limit <= 0:
        return []

    def sort_proc(collection: List[T]) -> None:
        idx_a = 0
        length = len(collection)
        while idx_a < length - 1:
            idx_b = idx_a + 1
            while idx_b < length:
                if collection[idx_a] > collection[idx_b]:
                    collection[idx_a], collection[idx_b] = collection[idx_b], collection[idx_a]
                idx_b += 1
            idx_a += 1

    sort_proc(data_container)

    def slice_func(coll: Sequence[T], start_idx: int, end_idx: int) -> List[T]:
        result_coll: List[T] = []
        cursor = start_idx
        while cursor < end_idx:
            result_coll.append(coll[cursor])
            cursor += 1
        return result_coll

    start = max(len(data_container) - count_limit, 0)
    end = len(data_container)
    return slice_func(data_container, start, end)