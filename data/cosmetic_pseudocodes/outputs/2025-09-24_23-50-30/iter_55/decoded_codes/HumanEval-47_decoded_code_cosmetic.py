from typing import Sequence, Union, List

def median(sequence: Sequence[Union[int, float]]) -> float:
    data: List[Union[int, float]] = list(sequence)  # make a mutable copy

    def sort_and_return(index_accumulator: int) -> None:
        if index_accumulator > len(data) - 2:
            return
        if data[index_accumulator] > data[index_accumulator + 1]:
            data[index_accumulator], data[index_accumulator + 1] = data[index_accumulator + 1], data[index_accumulator]
        sort_and_return(index_accumulator + 1)

    def bubble_pass(counter: int, max_count: int) -> None:
        if counter >= max_count:
            return
        sort_and_return(0)
        bubble_pass(counter + 1, max_count)

    n: int = len(data)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")

    bubble_pass(0, n - 1)

    half_point: int = n // 2

    if n % 2 == 1:
        return float(data[half_point])
    else:
        return (data[half_point - 1] + data[half_point]) / 2.0