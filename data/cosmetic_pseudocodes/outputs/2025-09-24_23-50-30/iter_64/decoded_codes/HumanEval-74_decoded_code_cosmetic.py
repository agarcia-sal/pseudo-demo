from typing import Iterable, Sequence, TypeVar, Union

T = TypeVar('T', bound=Sequence[str])

def total_match(param_a: T, param_b: T) -> T:
    def accumulate_length(index_accumulator: int, sum_accumulated: int, collection_param: T) -> int:
        if index_accumulator == len(collection_param):
            return sum_accumulated
        return accumulate_length(index_accumulator + 1, sum_accumulated + len(collection_param[index_accumulator]), collection_param)

    aggregator_one = accumulate_length(0, 0, param_a)
    aggregator_two = accumulate_length(0, 0, param_b)

    if aggregator_one <= aggregator_two:
        return param_a
    return param_b