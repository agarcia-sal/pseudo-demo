from typing import List, Sequence, TypeVar, Union

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    def compute_length(input_sequence: List[T], position: int, accumulator: int) -> int:
        if position < len(input_sequence):
            return compute_length(input_sequence, position + 1, accumulator + len(input_sequence[position]))
        return accumulator

    def calc_length(seq: List[T]) -> int:
        return compute_length(seq, 0, 0)

    sum_first = calc_length(list_one)
    sum_second = calc_length(list_two)

    return list_one if sum_first <= sum_second else list_two