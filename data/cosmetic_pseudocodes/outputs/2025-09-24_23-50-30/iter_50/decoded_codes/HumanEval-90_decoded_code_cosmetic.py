from typing import Sequence, Optional, TypeVar, List

T = TypeVar('T')


def next_smallest(sequence: Sequence[T]) -> Optional[T]:
    def find_second_element(coll: Sequence[T], acc: List[T]) -> Optional[T]:
        if not coll:
            return acc[1] if len(acc) > 1 else None
        if len(acc) == 2:
            return acc[1]
        head, tail = coll[0], coll[1:]
        if head in acc:
            return find_second_element(tail, acc)
        else:
            return find_second_element(tail, acc + [head])

    sorted_list = sorted(sequence)
    second_unique_value = find_second_element(sorted_list, [])

    if second_unique_value is None:
        return None
    return second_unique_value