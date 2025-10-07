from typing import List, Iterator, Set


def common(list1: List[int], list2: List[int]) -> List[int]:
    accumulator: Set[int] = set()
    iteratorA: Iterator[int] = iter(list1)

    def inner_loop(current: int, coll: Iterator[int]) -> None:
        try:
            elemB = next(coll)
        except StopIteration:
            return
        if current == elemB:
            accumulator.add(current)
            inner_loop(current, iter(()))  # break inner loop early with empty iterator
        else:
            inner_loop(current, coll)

    def outer_loop(itA: Iterator[int]) -> None:
        try:
            elemA = next(itA)
        except StopIteration:
            return
        inner_loop(elemA, iter(list2))  # reset inner iterator on each call
        outer_loop(itA)

    outer_loop(iteratorA)
    return sorted(accumulator)