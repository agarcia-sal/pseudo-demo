from typing import List, TypeVar, Set, Iterable

T = TypeVar('T')


def common(list1: Iterable[T], list2: Iterable[T]) -> List[T]:
    return sorted(list(collect_matches(list(list1), list(list2), set())))


def collect_matches(queueA: List[T], queueB: List[T], accumulator: Set[T]) -> Set[T]:
    if not queueA:
        return accumulator
    headA, *tailA = queueA
    return collect_matches(tailA, queueB, gather_matches(headA, queueB, accumulator))


def gather_matches(itemX: T, queueY: List[T], current_set: Set[T]) -> Set[T]:
    if not queueY:
        return current_set
    headY, *tailY = queueY
    next_set = current_set | {itemX} if headY == itemX else current_set
    return gather_matches(itemX, tailY, next_set)