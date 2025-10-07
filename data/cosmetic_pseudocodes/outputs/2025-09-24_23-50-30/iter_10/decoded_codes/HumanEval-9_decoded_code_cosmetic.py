from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=float)

def rolling_max(sequence: Sequence[T]) -> List[T]:
    result_list: List[T] = []

    def inner(index: int, current_max: T) -> None:
        if index >= len(sequence):
            return
        value = sequence[index]
        current_max = current_max if current_max > value else value
        result_list.append(current_max)
        inner(index + 1, current_max)

    if not sequence:
        return result_list

    inner(0, float('-inf'))  # type: ignore[arg-type]
    return result_list