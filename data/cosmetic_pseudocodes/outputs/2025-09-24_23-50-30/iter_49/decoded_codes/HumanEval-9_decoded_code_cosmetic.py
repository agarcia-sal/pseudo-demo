from typing import Iterable, List, Optional, TypeVar

T = TypeVar("T")


def rolling_max(collection_of_values: Iterable[T]) -> List[T]:
    def accumulate_leading_maximums(
        source: List[T], accumulator: List[T], current_best: Optional[T], index: int
    ) -> List[T]:
        if index >= len(source):
            return accumulator
        candidate = source[index]
        new_best = (
            candidate
            if current_best is None or candidate > current_best
            else current_best
        )
        return accumulate_leading_maximums(
            source, accumulator + [new_best], new_best, index + 1
        )

    src_list = list(collection_of_values)
    return accumulate_leading_maximums(src_list, [], None, 0)