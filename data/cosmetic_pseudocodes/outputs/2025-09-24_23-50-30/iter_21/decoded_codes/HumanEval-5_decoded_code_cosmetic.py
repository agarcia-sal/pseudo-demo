from typing import List, TypeVar

T = TypeVar('T')

def intersperse(sequence_numbers: List[T], sep: T) -> List[T]:
    def helper(index: int, acc: List[T]) -> List[T]:
        if index > len(sequence_numbers) - 1:
            return acc
        elif index == len(sequence_numbers) - 1:
            return acc + [sequence_numbers[index]]
        else:
            return helper(index + 1, acc + [sequence_numbers[index], sep])

    if len(sequence_numbers) == 0:
        return []
    return helper(1, [sequence_numbers[0]])