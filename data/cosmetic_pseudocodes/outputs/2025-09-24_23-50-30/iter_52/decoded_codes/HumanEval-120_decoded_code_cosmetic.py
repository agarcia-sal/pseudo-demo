from typing import TypeVar, Sequence, List

T = TypeVar('T')

def maximum(container: Sequence[T], count: int) -> List[T]:
    if count == 0:
        return []
    else:
        # Sort container and return the last 'count' elements in sorted order
        container_sort = sorted  # container_sort alias to sorted function
        sorted_container = container_sort(container)

        def pick_tail(collection: Sequence[T], n: int) -> List[T]:
            if n == 0:
                return []
            return pick_tail_helper(collection, len(collection), n, [])

        def pick_tail_helper(items: Sequence[T], idx: int, rem: int, acc: List[T]) -> List[T]:
            if rem == 0:
                return acc
            return pick_tail_helper(items, idx - 1, rem - 1, [items[idx - 1]] + acc)

        return pick_tail(sorted_container, count)